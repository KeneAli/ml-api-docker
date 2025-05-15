FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code into container
COPY . .

# Tell Python to look for packages in /app
ENV PYTHONPATH=/app

# Expose the port
EXPOSE 5000

# Run your Flask app
CMD ["python", "api/app.py"]
