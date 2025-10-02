FROM python:3.9-slim

WORKDIR /app

COPY util/requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app 

ENTRYPOINT ["python3", "main.py"]