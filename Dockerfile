# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Copy the application code into the container
COPY . .

# Expose the port that the application will run on
EXPOSE 5001

# Set environment variables
ENV FLASK_APP=run.py
ENV REDIS_HOST=redis-service
ENV REDIS_PORT=6379

# Add healthcheck
HEALTHCHECK CMD curl --fail http://localhost:5001/health || exit 1

# Run the application
CMD ["python", "run.py"]
