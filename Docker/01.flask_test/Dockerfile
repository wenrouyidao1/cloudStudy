FROM python:3.6.4
COPY ./main.py /app/main.py
COPY ./registry.conf /app/registry.conf
WORKDIR /app
RUN mkdir /root/.pip
COPY ./pip.conf /root/.pip/pip.conf
RUN pip3 install requests && pip3 install flask
CMD python3 main.py