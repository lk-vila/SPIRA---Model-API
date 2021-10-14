FROM python:3.9.7

WORKDIR /usr/src/spira-api

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "api.py" ]