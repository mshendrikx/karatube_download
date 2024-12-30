# Use Ubuntu 22.04 base image
FROM ubuntu:22.04

# Install packages
RUN apt-get update && apt-get install -y python3-pip apt-transport-https nano curl

WORKDIR /app

COPY requirements.txt . 

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

RUN mkdir download

# Expose port 7006 for web traffic
EXPOSE 7006

# Start pyhton app in the foreground
CMD ["python3", "/app/app.py"]