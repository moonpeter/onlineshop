#!/usr/bin/env sh
IDENTITY_FILE="$HOME/.ssh/onlineshop.pem"
USER="ubuntu"
HOST="15.165.204.216"
TARGET=${USER}@${HOST}
ORIGIN_SOURCE="$HOME/projects/portfolio/onlineshop/"
DEST_SOURCE="/home/ubuntu/projects/"
SSH_CMD="ssh -i ${IDENTITY_FILE} ${TARGET}"

echo "== runserver 배포 =="

# 서버 초기설정
echo "apt update & upgrade & autoremove 111111111111111"
${SSH_CMD} -C 'sudo apt update && sudo DEBIAN_FRONTEND=noninteractive apt dist-upgrade -y && apt -y autoremove'
echo "apt install python3-pip 22222222222222222222"
${SSH_CMD} -C 'sudo apt -y install python3-pip'

# pip freeze
echo "pip freeze 3333333333333333333"
"$HOME"/.pyenv/versions/3.7.4/envs/onlineshop/bin/pip freeze > "$HOME"/projects/portfolio/onlineshop/requirements.txt

# 기존 폴더 삭제
echo "remove server source 44444444444444"
${SSH_CMD} sudo rm -rf ${DEST_SOURCE}

# 로컬에 있는 파일 업로드
echo "upload local source 5555555555555555555"
${SSH_CMD} mkdir -p ${DEST_SOURCE}
scp -q -i "${IDENTITY_FILE}" -r "${ORIGIN_SOURCE}" ${TARGET}:${DEST_SOURCE}

# pip install
echo "pip install 666666666666666666"
${SSH_CMD} pip3 install -q -r /home/ubuntu/projects/onlineshop/requirements.txt

echo "screen settings 77777777777777777777"
# 실행중이던 screen 세션종료
${SSH_CMD} -C 'screen -X -S runserver quit'
# screen 실행
${SSH_CMD} -C 'screen -S runserver -d -m'
# 실행중인 세션에 명령어 전달
${SSH_CMD} -C "screen -r runserver -X stuff 'sudo python3 /home/ubuntu/projects/onlineshop/app/manage.py runserver 0:80\n'"

echo "  finish!!!!!!!!!!!!!!!!!!!!!!!!"