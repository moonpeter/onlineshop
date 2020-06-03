# onlineshop(온라인 쇼핑몰 사이트)

domain : https://moonpeter.com

github : https://github.com/moonpeter/onlineshop



## Package

```
python = "^3.7"
django = ">3.0"
psycopg2-binary = "^2.8.5"
boto3 = "^1.13.13"
django-storages = "^1.9.1"
gunicorn = "^20.0.4"
supervisor = "^4.2.0"
pillow = "^7.1.2"
django-allauth = "^0.41.0"
requests = "^2.23.0"
```



## Installation

- package management
  - use poetry

**`Poetry Install`**

```
# osx, linux
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# windows
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

**`package install`**

- $poetry install
- $pip install -r requirements.txt



## ERD

URL : https://aquerytool.com:443/aquerymain/index/?rurl=b7ed4b73-55de-4d54-80df-6f0c33776011&

- Password : 1gspm1

![image](https://user-images.githubusercontent.com/57426244/83367549-0d5e8c00-a3f0-11ea-82e3-299af4c10eee.png)



## 배포 과정

https://drive.google.com/file/d/122sqhHRFdhF9RFZ3UwjpAUwLQpM4L46h/view?usp=sharing

![image](https://user-images.githubusercontent.com/57426244/83371560-af38a580-a3fd-11ea-9040-c60ec1b4eae4.png)











## 1. 메인페이지

<img src="https://user-images.githubusercontent.com/57426244/83587847-fe601100-a58a-11ea-9ffe-13d702a5ae67.png" alt="image" style="zoom:25%;" />



## 2. 로그인 / 소셜로그인(네이버) / 로그아웃 페이지

<img src="https://user-images.githubusercontent.com/57426244/83347275-0cc9e500-a35f-11ea-9672-8e931326ac65.png" alt="image" style="zoom:25%;" />

<img src="https://user-images.githubusercontent.com/57426244/83347303-3f73dd80-a35f-11ea-81d2-b207a6badfb4.png" alt="image" style="zoom:25%;" />

<img src="https://user-images.githubusercontent.com/57426244/83347343-5fa39c80-a35f-11ea-88e0-2c29f619ad43.png" alt="image" style="zoom:25%;" />

## 3. 상품의 상세페이지

<img src="https://user-images.githubusercontent.com/57426244/83344880-b3a28700-a347-11ea-9f83-d40aca22ffeb.png" alt="image" style="zoom:25%;" />

## 4. 카트 상세페이지

<img src="https://user-images.githubusercontent.com/57426244/83344881-ba30fe80-a347-11ea-9c0c-afab7148bb6f.png" alt="image" style="zoom:25%;" />



## 5. 주문 페이지

<img src="https://user-images.githubusercontent.com/57426244/83344885-c9b04780-a347-11ea-8918-b71c0ea7b92b.png" alt="image" style="zoom:25%;" />

## 6. 결제 페이지

<img src="https://user-images.githubusercontent.com/57426244/83344887-d16fec00-a347-11ea-9d66-3975322d98e1.png" alt="image" style="zoom:25%;" />
