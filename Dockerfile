FROM python:alpine

EXPOSE 5000

WORKDIR /srv/contacts_app_backend

COPY ./requirements.txt .

RUN \
pip install --no-cache-dir --upgrade pip setuptools pip && \
# TODO: Костыль который позволяет установить пакет flask-mongoengine. Проверить в будущем необходимость
#       ручной установки данного пакета:
pip install --no-cache-dir --default-timeout=60 rednose && \
pip install --no-cache-dir -r requirements.txt

WORKDIR /srv/contacts_app_backend

COPY . .

ENV FLASK_ENV=development FLASK_DEBUG=0 FLASK_APP=backend

CMD flask run --host 0.0.0.0 --port 5000
