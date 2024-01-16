# Use an official lightweight Python image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the local code to the container
COPY . /app

# Install the dependencies, including NumPy
RUN pip install --no-cache-dir fastapi uvicorn Pillow numpy torch

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
