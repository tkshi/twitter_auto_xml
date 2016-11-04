FROM ubuntu:latest
MAINTAINER Rajdeep Dua "dua_rajdeep@yahoo.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]
