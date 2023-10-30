#!/bin/bash
docker stop postgres
docker container prune
docker run --name postgres --network host -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres
sleep 20s
# docker exec -t postgres pg_dumpall -c -U postgres > medpoisk.sql
cat medpoisk.sql | docker exec -i postgres psql -U postgres