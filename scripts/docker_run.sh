#!/bin/bash
docker stop postgres
docker container prune
docker run --name postgres --network host -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres
