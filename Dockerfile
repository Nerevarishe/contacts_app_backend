FROM python:alpine

WORKDIR /

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /srv/contacts_app_backend

CMD gunicorn -w 4 -b 0.0.0.0:5000 backend:app
