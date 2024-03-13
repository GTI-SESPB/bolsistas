#!/bin/sh

python -m flask --app src.wsgi:app db upgrade &&\
python -m gunicorn -w 4 -b 0.0.0.0 "src.wsgi:app"
