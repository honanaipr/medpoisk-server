FROM python:3.11-slim

RUN apt update && apt upgrade -y && apt install -y libpq-dev python3-dev gcc

RUN pip install -U pip && pip install poetry

WORKDIR /medpoisk-server

COPY ./pyproject.toml .

RUN poetry install --no-root

COPY . .

CMD poetry run python -m medpoisk_server
