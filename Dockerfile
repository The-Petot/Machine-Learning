# Use Python slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies and Google Cloud SDK
RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    ca-certificates \
    gnupg \
    && echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - \
    && apt-get update && apt-get install -y google-cloud-sdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .

# Copy Google Cloud credentials
COPY ServiceAccount.json .

# Create startup script
RUN echo '#!/bin/bash\n\
    gcloud auth activate-service-account --key-file=ServiceAccount.json\n\
    uvicorn main:app --host 0.0.0.0 --port 8000' > start.sh

# Make script executable
RUN chmod +x start.sh

# Expose port
EXPOSE 8000

# Set environment variable
ENV PYTHONUNBUFFERED=1
ENV SYSTEM_INSTRUCTION = 
ENV LOCATION = 
ENV PROJECT_ID = 
ENV AI_MODEL = 

# Run startup script
ENTRYPOINT ["./start.sh"]