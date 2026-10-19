cat << 'EOF' > deploy.sh
#!/bin/bash
echo "Deploying CityCare SOC Pipeline..."
sudo docker-compose pull
sudo docker-compose up -d
echo "Deployment complete. System is running."
EOF
chmod +x deploy.sh
