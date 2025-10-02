FROM python:3.13.7-slim

WORKDIR /app

COPY util/requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app 

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]