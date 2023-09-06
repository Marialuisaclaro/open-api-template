#!/bin/sh

# Bail run on process fail
set -o errexit
set -o nounset

# Handle sigterm gracefully
term_handler() {
  if [ $pid -ne 0 ]; then
    kill -SIGTERM "$pid"
    wait "$pid"
  fi
  exit 143;
}

trap term_handler TERM

# This should be taken care of by the deployment tools for production
if [ "$DEBUG" = "True" ]
then
  export PYTHONBREAKPOINT=ipdb.set_trace
  poetry install
  python manage.py migrate

  until uvicorn conf.asgi:application --lifespan off --reload --port 8000 --host 0.0.0.0; do
    echo "Development server crashed... restarting" >&2
    sleep 3;
  done

  elif [ "${TESTING}" = "True" ]; then
    export DEBUG=True
    pytest -v --cov-report term-missing --cov-fail-under=100 --cov=.
  else
    python manage.py migrate
    uvicorn conf.asgi:application --lifespan off --port 8000 --host 0.0.0.0
fi
