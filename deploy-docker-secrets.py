#!/usr/bin/env python

# 1. Host에서 이미지 build, push
# 2. EC2에서 이미지 pull, run(bash)
# 3. Host -> EC2 -> Container로 secrets.json전송
# 4. Container에서 runserver

import os
import subprocess
from pathlib import Path

DOCKER_IMAGE_TAG = 'moonpeter/onlineshop'
DOCKER_OPTIONS = [
    ('--rm', ''),
    ('-it', ''),
    # background로 실행하는 옵션 추가
    ('-d', ''),
    ('-p', '80:8000'),
    ('--name', 'onlineshop'),
]
USER = 'ubuntu'
HOST = "15.165.204.216"
TARGET = f'{USER}@{HOST}'
HOME = str(Path.home())
IDENTITY_FILE = os.path.join(HOME, '.ssh', 'onlineshop.pem')
SOURCE = os.path.join(HOME, 'projects', 'portfolio', 'onlineshop')
SECRETS_FILE = os.path.join(SOURCE, 'secrets.json')


def run(cmd, ignore_error=False):
    process = subprocess.run(cmd, shell=True)
    if not ignore_error:
        process.check_returncode()


def ssh_run(cmd, ignore_error=False):
    run(f"ssh -o StrictHostKeyChecking=no -i {IDENTITY_FILE} {TARGET} -C {cmd}", ignore_error=ignore_error)


# 1. 호스트에서 도커 이미지 build, push
def local_build_push():
    run(f'docker build -t {DOCKER_IMAGE_TAG} .')
    run(f'docker push {DOCKER_IMAGE_TAG}')
    print('1111111111111111111')


# 서버 초기설정
def server_init():
    ssh_run(f'sudo apt update')
    ssh_run(f'sudo DEBIAN_FRONTEND=noninteractive apt dist-upgrade -y')
    ssh_run(f'sudo apt -y install docker.io')


# 2. 실행중인 컨테이너 종료, pull, run
def server_pull_run():
    ssh_run(f'sudo docker stop onlineshop', ignore_error=True)
    ssh_run(f'sudo docker pull {DOCKER_IMAGE_TAG}')
    ssh_run('sudo docker run {options} {tag} /bin/bash'.format(
        options=' '.join([
            f'{key} {value}' for key, value in DOCKER_OPTIONS
        ]),
        tag=DOCKER_IMAGE_TAG,
    ))
    print('222222222222222222222')


# 3. Host에서 EC2로 secrets.json을 전송, EC2에서 Container로 다시 전송
def copy_secrets():
    run(f'scp -i {IDENTITY_FILE} {SECRETS_FILE} {TARGET}:/tmp', ignore_error=True)
    ssh_run(f'sudo docker cp /tmp/secrets.json onlineshop:/srv/onlineshop')
    print('33333333333333333333333333')


# 4. Container에서 runserver실행
def server_runserver():
    ssh_run(f'sudo docker exec -it -d onlineshop '
            f'python /srv/onlineshop/app/manage.py runserver 0:8000')
    print('4444444444444444')


if __name__ == '__main__':
    try:
        local_build_push()
        server_init()
        server_pull_run()
        copy_secrets()
        server_runserver()
    except subprocess.CalledProcessError as e:
        print('deploy-docker-secrets Error!')
        print(' cmd:', e.cmd)
        print(' returncode:', e.returncode)
        print(' output:', e.output)
        print(' stdout:', e.stdout)
        print(' stderr:', e.stderr)