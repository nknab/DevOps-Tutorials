FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

WORKDIR /app
COPY ./Final .

CMD ["python3", "main.py"]