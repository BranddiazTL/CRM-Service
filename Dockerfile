# Pull base python image
FROM python:3.10.2-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /CRM-Service
COPY . .

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Limit the scope of user who run the docker image
RUN adduser user
USER user