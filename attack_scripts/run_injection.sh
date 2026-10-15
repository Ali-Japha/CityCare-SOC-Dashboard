#!/bin/bash
echo "Simulating SQL Injection via sqlmap..."
docker run --rm secsi/sqlmap -u "http://httpbin.org/get?id=1" --batch
echo "Generating corresponding Elasticsearch logs..."
cat << 'LOG_EOF' >> ../public/logs.json
{"timestamp": "2026-10-16T12:05:01Z", "level": "ERROR", "message": "Database error: syntax error near 'OR 1=1'"}
{"timestamp": "2026-10-16T12:05:02Z", "level": "ERROR", "message": "Database error: unclosed quotation mark after character string"}
{"timestamp": "2026-10-16T12:05:03Z", "level": "ERROR", "message": "Database error: SQL syntax error near 'UNION SELECT'"}
{"timestamp": "2026-10-16T12:05:04Z", "level": "ERROR", "message": "Database error: syntax error near '--'"}
{"timestamp": "2026-10-16T12:05:05Z", "level": "ERROR", "message": "Database error: unclosed quotation mark"}
LOG_EOF
echo "SQL injection simulation complete."
