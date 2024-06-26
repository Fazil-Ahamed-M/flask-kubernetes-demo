# Use an official Python runtime as a parent image
FROM python:3.9.5-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the Flask application files
COPY main.py /app/
COPY requirements.txt /app/

# Copy the static and templates directories
COPY static/ /app/static/
COPY templates/ /app/templates/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define the command to run your application
CMD ["python", "main.py"]
