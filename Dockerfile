FROM --platform=linux/amd64 python:3.9-slim

RUN mkdir -p /app

WORKDIR /app

COPY . ./

COPY requeriments.txt ./

RUN pip install -r requeriments.txt

#CMD ["python", "main.py"]