FROM python:3.11 AS build

RUN pip install poetry

WORKDIR /medpoisk-server

COPY . .

RUN poetry build --directory=dist --no-interaction

RUN ./scripts/gen_token.sh


FROM python:3.11-alpine

WORKDIR /medpoisk-server

COPY --from=build /medpoisk-server/dist/*.whl .

RUN python -m pip install *.whl

ENV ROOT_PATH /medpoisk-server/

COPY --from=build /medpoisk-server/scripts/*.pem ./scripts/
RUN ls ./scripts/

CMD [ "medpoisk_server_run" ]
