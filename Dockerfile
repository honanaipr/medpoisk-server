FROM python:3.11 AS build

RUN pip install poetry

WORKDIR /medpoisk-server

COPY ./pyproject.toml .

RUN poetry install --no-root

COPY . .

RUN poetry build --directory=dist --no-interaction

RUN ./scripts/gen_token.sh


FROM python:3.11-alpine

WORKDIR /medpoisk-server

COPY --from=build /medpoisk-server/dist/*.whl .

RUN pip install *.whl

ENV ROOT_PATH /medpoisk-server/

COPY --from=build /medpoisk-server/scripts/*.pem ./scripts/

CMD [ "medpoisk_server_run" ]
