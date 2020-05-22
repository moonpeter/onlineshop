FROM        python:3.7-slim

RUN         apt -y update && apt -y dist-upgrade

# poetry export로 생성된 reuirements.txt를 적절히 복사
COPY        ./requirements.txt /tmp/
RUN         pip install -r /tmp/requirements.txt

# 소스코드 복사 후 runserver
COPY        . /srv/onlineshop
WORKDIR     /srv/onlineshop/app
CMD         python manage.py runserver 0:8000