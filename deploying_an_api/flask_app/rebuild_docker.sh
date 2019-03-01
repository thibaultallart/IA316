#!/usr/bin/env bash
docker stop flask_app_debbug_mode
docker rm flask_app_debbug_mode
docker rmi flask_app_debbug_mode
docker build -t flask_app_debbug_mode .
docker run -d -p 5001:5000 --name flask_app_debbug_mode flask_app_debbug_mode
