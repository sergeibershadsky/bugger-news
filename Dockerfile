FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10

RUN apk update && apk add gcc libffi-dev g++ postgresql-dev make curl libxml2 libxml2-dev libxslt libxslt-dev

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY pyproject.toml poetry.lock* /

RUN poetry install --no-root --no-dev

RUN apk del libffi-dev g++ make curl libxml2-dev libxslt-dev

COPY ./app /app/app
