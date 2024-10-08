# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port that the application will run on
EXPOSE 5001

# Set the environment variable for Flask
ENV FLASK_APP=run.py

# Run the application
CMD ["python", "run.py"]
