FROM 10.36.145.100:5000/centos7_python3:v1.0-turbo
COPY nginx.repo /etc/yum.repos.d/nginx.repo
RUN yum -y install nginx && rm -rf /usr/share/nginx/html/*
COPY html/* /usr/share/nginx/html/

WORKDIR /usr/share/nginx/html
CMD nginx && python3 main.py && tailf /dev/null