import json
import requests
import time
import urllib3

# Suppress insecure HTTPS warnings for our self-signed cert
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ES_URL = "https://localhost:9200"
INDEX = "citycare-logs"
AUTH = ("elastic", "citycare_pass")
HEADERS = {"Content-Type": "application/json"}

# 1. Inject Test Data
test_logs = [
    # Benign logs
    {"timestamp": "2026-10-12T10:00:00Z", "level": "INFO", "message": "User admin logged in successfully."},
    {"timestamp": "2026-10-12T10:01:00Z", "level": "INFO", "message": "Dashboard accessed."},
    # SQLi payload log
    {"timestamp": "2026-10-12T10:02:00Z", "level": "ERROR", "message": "Database error: You have an error in your SQL syntax near '1=1'."},
    # Brute force logs (>5 within 2 mins)
    {"timestamp": "2026-10-12T10:03:01Z", "level": "WARN", "message": "failed login from 192.168.1.100"},
    {"timestamp": "2026-10-12T10:03:05Z", "level": "WARN", "message": "failed login from 192.168.1.100"},
    {"timestamp": "2026-10-12T10:03:10Z", "level": "WARN", "message": "failed login from 192.168.1.100"},
    {"timestamp": "2026-10-12T10:03:15Z", "level": "WARN", "message": "failed login from 192.168.1.100"},
    {"timestamp": "2026-10-12T10:03:20Z", "level": "WARN", "message": "failed login from 192.168.1.100"},
    {"timestamp": "2026-10-12T10:03:25Z", "level": "WARN", "message": "failed login from 192.168.1.100"}
]

print("Injecting test logs into Elasticsearch...")
for log in test_logs:
    requests.post(f"{ES_URL}/{INDEX}/_doc", auth=AUTH, headers=HEADERS, json=log, verify=False)

# Force index refresh to make data immediately searchable
requests.post(f"{ES_URL}/{INDEX}/_refresh", auth=AUTH, verify=False)
time.sleep(1)

# 2. Evaluate Rules
report_lines = ["CityCare Detection Validation Report\n==================================\n"]

def evaluate_rule(file_path):
    with open(file_path, 'r') as f:
        rule = json.load(f)
    
    es_query = {"query": rule["query"]}
    response = requests.get(f"{ES_URL}/{INDEX}/_search", auth=AUTH, headers=HEADERS, json=es_query, verify=False)
    hits = response.json().get("hits", {}).get("total", {}).get("value", 0)
    
    status = "PASS" if hits >= rule["threshold"] else "FAIL"
    result = f"Rule: {rule['rule_name']}\nMITRE: {rule['mitre_attack']['technique_id']}\nHits: {hits} (Threshold: {rule['threshold']})\nResult: {status}\n\n"
    print(result.strip())
    report_lines.append(result)

print("\nEvaluating Detection Rules...")
evaluate_rule("rules/brute_force_rule.json")
evaluate_rule("rules/sql_injection_rule.json")

# 3. Output Report
with open("test_report.txt", "w") as f:
    f.writelines(report_lines)
print("Validation complete. Report saved to test_report.txt.")
