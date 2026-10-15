#!/bin/bash
echo "Simulating Brute Force Attack via Hydra..."
# Using a public test endpoint to generate dummy network traffic
docker run --rm secsi/hydra -l admin -p password123 http-get://httpbin.org/basic-auth/admin/password123
echo "Generating corresponding Elasticsearch logs..."
cat << 'LOG_EOF' >> ../public/logs.json
{"timestamp": "2026-10-16T12:00:01Z", "level": "WARN", "message": "failed login from 10.0.0.50"}
{"timestamp": "2026-10-16T12:00:02Z", "level": "WARN", "message": "failed login from 10.0.0.50"}
{"timestamp": "2026-10-16T12:00:03Z", "level": "WARN", "message": "failed login from 10.0.0.50"}
{"timestamp": "2026-10-16T12:00:04Z", "level": "WARN", "message": "failed login from 10.0.0.50"}
{"timestamp": "2026-10-16T12:00:05Z", "level": "WARN", "message": "failed login from 10.0.0.50"}
{"timestamp": "2026-10-16T12:00:06Z", "level": "WARN", "message": "failed login from 10.0.0.50"}
{"timestamp": "2026-10-16T12:00:07Z", "level": "WARN", "message": "failed login from 10.0.0.50"}
{"timestamp": "2026-10-16T12:00:08Z", "level": "WARN", "message": "failed login from 10.0.0.50"}
{"timestamp": "2026-10-16T12:00:09Z", "level": "WARN", "message": "failed login from 10.0.0.50"}
{"timestamp": "2026-10-16T12:00:10Z", "level": "WARN", "message": "failed login from 10.0.0.50"}
LOG_EOF
echo "Brute force simulation complete."
