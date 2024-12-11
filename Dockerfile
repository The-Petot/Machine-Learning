# Use Python slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy model files
COPY summarization_model/ ./summarization_model/

# Copy application code and environment file
COPY main.py .

# Expose the port
EXPOSE 8000

# Env
ENV PUBSUB_TOPIC=

# Run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

