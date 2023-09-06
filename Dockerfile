FROM python:3.10-slim-buster

# Ensures our console output looks familiar and is not buffered by Docker.
ENV PYTHONUNBUFFERED 1

# Will not get prompted for input
ARG DEBIAN_FRONTEND=noninteractive

# Update repos and upgrade packages
RUN apt-get update -qq
RUN apt-get upgrade -yq

# Install apt-utils so debian will not complain about delaying configurations
RUN apt-get install -yq --no-install-recommends apt-utils

# Install basic SO dependencies
RUN apt-get install -yq gcc python3-dev libpq-dev postgresql-client

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install and configure poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false

# Copy poetry files first and install dependencies
# This is done earlier to avoid installing all dependencies
# when changing code and building the image
RUN mkdir /src
COPY ./src/poetry.lock /src/poetry.lock
COPY ./src/pyproject.toml /src/pyproject.toml
WORKDIR /src
RUN poetry install --only main

# Finally copy the app and devops-related stuff
COPY ./src /src
COPY ./devops /devops

# Run the entrypoint. This will migrate the db and run the app in uvicorn.
ENTRYPOINT [ "/devops/entrypoint.sh" ]
