#!/bin/sh
set -e

echo "Starting the Planning poker server"
export FLASK_ENV=development
export FLASK_APP=web/app.py
flask run -h 0.0.0.0 -p 9000
