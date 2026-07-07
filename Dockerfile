FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose FastAPI default port inside network matrix
EXPOSE 8000

# Run asynchronous production web server loop
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
