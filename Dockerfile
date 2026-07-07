# Step 1: Base Linux OS image with Python 3.10 pre-installed
FROM python:3.10-slim

# Step 2: Set working directory inside the virtual container
WORKDIR /app

# Step 3: Copy dependency mapping first (Optimizes Docker layer caching)
COPY requirements.txt .

# Step 4: Install system and python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy all our repository pipeline files into the container
COPY . .

# Master script ko execution permissions dena zaroori hy
RUN chmod +x run_pipeline.sh

# Target our orchestration script instead of a single file
CMD ["./run_pipeline.sh"]
