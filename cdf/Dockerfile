# Start with Python base image
FROM python:3.8-slim

# Create working directory
WORKDIR /usr/src

# Install Python packages
COPY requirements.txt .
RUN pip install --upgrade pip==21.3.1
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script files to the container's working directory
COPY codes/ .

# Run script
CMD ["python3", "Geocoding.py"] # Replace "<my_script>.py" with the actual name of your Python script
