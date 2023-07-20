
# Start with Python base image
FROM python:3.8-slim

# Create working directory
WORKDIR /usr/src


# Install Python packages
COPY requirements.txt .
RUN pip install --upgrade pip==21.3.1
RUN pip install --no-cache-dir -r requirements.txt


COPY scripts/


# Run script
CMD ["python3", "<my_script>.py"] # This is running as a Python script, not a module
