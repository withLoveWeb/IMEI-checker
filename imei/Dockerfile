FROM python:3.13-slim

ENV POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local'


RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
      curl \
  && curl -sSL 'https://install.python-poetry.org' | python - \
  && poetry --version \
  # Clean cache
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./poetry.lock ./pyproject.toml /app/

RUN poetry install --no-root

COPY ./imei /app/imei

CMD [ ]
