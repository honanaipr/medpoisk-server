#!/bin/bash
# docker exec -t postgres pg_dump -U postgres > medpoisk.sql
cat medpoisk.sql | docker exec -i postgres psql -U postgres
