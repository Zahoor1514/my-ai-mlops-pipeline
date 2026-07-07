#!/bin/bash
set -e

CONTAINER_NAME="mlops-live-api"
IMAGE_NAME="ghcr.io/zahoor1514/ai-mlops-engine:latest"

echo "🔄 [CD Pipeline] Pulling fresh production image from GitHub Container Registry..."
sudo docker pull $IMAGE_NAME

# Check if old container exists and remove it safely
if [ "$(sudo docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "⚠️ [CD Pipeline] Found older container instantiation. Cleaning up environment..."
    sudo docker stop $CONTAINER_NAME || true
    sudo docker rm $CONTAINER_NAME || true
fi

echo "🚀 [CD Pipeline] Spinning up enterprise container matrix on Network Node Port 8000..."
sudo docker run -d \
  -p 8000:8000 \
  --name $CONTAINER_NAME \
  --restart always \
  $IMAGE_NAME

echo "🟢 [CD Pipeline] Microservice successfully upgraded and hot-reloaded!"
sudo docker ps -f name=$CONTAINER_NAME
