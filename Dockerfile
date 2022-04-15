FROM python:3.8

WORKDIR /app

ADD . /app

EXPOSE 80

CMD ["python3", "main.py"]