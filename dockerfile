# Use the official Python image as the base image
FROM python:3.9

# Set environment variables
ENV WEB2PY_VERSION=2.24.1
ENV WEB2PY_ROOT=/opt/web2py

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends wget unzip \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /opt/web2py

# Copy the web2py source code into the image
COPY . .

# Expose the port web2py runs on
EXPOSE 8000

# Set permissions and start web2py
CMD ["python", "web2py.py", "-a", "admin", "-i", "0.0.0.0", "-p", "8000"]

