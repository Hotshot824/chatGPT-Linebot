FROM python:3.10-bullseye

LABEL maintainer="benson"

WORKDIR /root/
ADD ./requirements.txt /root/

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && apt-get -y upgrade

RUN python3 -m pip install -r requirements.txt \ 
&& rm requirements.txt

RUN useradd -u 1000 -ms /bin/bash linebot && usermod -aG sudo linebot
USER linebot

WORKDIR /home/linebot

EXPOSE 8000

CMD ["python3"]