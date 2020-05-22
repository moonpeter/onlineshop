FROM        python:3.7-slim

RUN         apt -y update && apt -y dist-upgrade && apt -y autoremove
RUN         apt -y install nginx

# poetry export로 생성된 reuirements.txt를 적절히 복사
COPY        ./requirements.txt /tmp/
RUN         pip install -r /tmp/requirements.txt

# 소스코드 복사
COPY        . /srv/onlineshop
WORKDIR     /srv/onlineshop/app

# Nginx설정파일을 복사
RUN         cp /srv/onlineshop/.config/onlineshop.nginx /etc/nginx/sites-enabled/