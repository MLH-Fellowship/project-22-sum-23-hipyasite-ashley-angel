#!/bin/bash

cd ~/project-22-sum-23-hipyasite-ashley-angel
git fetch && git reset origin/main --hard
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build