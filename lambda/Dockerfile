# Use Python 3.9 runtime (compatible with AWS Lambda)
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY lambda_function.py .

# Command to run the Lambda function (for local testing)
CMD ["python", "lambda_function.py"]
