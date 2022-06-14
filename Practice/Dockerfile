FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

RUN echo "I am run during image building"

WORKDIR /app
COPY . .

CMD ["python3", "app.py"]