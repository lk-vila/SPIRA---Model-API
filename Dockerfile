FROM python:3.9.7

WORKDIR /usr/src/spira-api

COPY . .

RUN chmod +x scripts/*

RUN bash scripts/get_resources.sh

RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE 5000

ENTRYPOINT [ "uwsgi", "config/uwsgi.ini" ]