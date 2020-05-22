daemon = False
chdir = '/srv/onlineshop/app'
bind = 'unix:/run/onlineshop.sock'
accesslog = '/var/log/gunicorn/onlineshop-access.log'
errorlog = '/var/log/gunicorn/onlineshop-error.log'
capture_output = True
