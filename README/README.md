<h1 align="center">A backend template</h1>

This is a template for writing APIs. Technically, it is:

- A [Django](https://www.djangoproject.com/)-based application
- Built with [django-ninja](https://django-ninja.rest-framework.com/)
- Running in [Docker](https://www.docker.com/)
- Using a [PostgreSQL](https://www.postgresql.org/) database
- Developed with [Docker compose](https://docs.docker.com/compose/)

## Dependencies

The only dependency to run this project is [Docker Compose V2](https://docs.docker.com/compose/cli-command/), which comes by default with [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/). If you want to run the project without Docker you can also install [Poetry](https://python-poetry.org/) and run the Django app in `/src` directly. You'll need a Postgres database and some environment configuration. We recommend Docker, but up to you.

## Run & try

You should be able to run the project by simply executing `make dev` (make sure Docker is running). The first time this might take a minute or two depending on your connection speed.

Once everything is ready you should see the following in your terminal.

```bash
openapi-template     | INFO:     Started server process [111]
openapi-template     | INFO:     Waiting for application startup.
openapi-template     | INFO:     ASGI 'lifespan' protocol appears unsupported.
openapi-template     | INFO:     Application startup complete.
```

Now you can interact with the API in [localhost:8000/api/docs](http://localhost:8000/api/docs). Success 🚀!

## Local commands

This project uses [GNU make](https://www.gnu.org/software/make/manual/make.html) to simplify running local commands inside the development container. To see all available commands you can inspect [the Makefile](./Makefile).

## Developing guides

- @TODO [Folder architecture](./README/dev/folder-architecture.md)
- @TODO [Testing](./README/dev/testing.md)
- @TODO [Linting & Formatting](./README/dev/linting-and-formatting.md)

## You a wizard 🧙?

- @TODO [Continuous integration](./README/devops/CI.md)
- @TODO [Deploying to Cloud Run](./README/devops/cloud-run-deploy.md)
