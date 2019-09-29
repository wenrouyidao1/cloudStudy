FROM python:3.6.4
COPY . /app
WORKDIR /app
RUN mkdir /root/.pip
COPY pip.conf /root/.pip/pip.conf
RUN pip3 install -r req.txt

EXPOSE 8000
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
