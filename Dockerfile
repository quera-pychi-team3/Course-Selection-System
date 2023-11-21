FROM python:3.11.6-slim-bookworm

RUN mkdir -p /app

RUN addgroup --system app && adduser --system --group app

ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y --no-install-recommends netcat

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x  $APP_HOME/entrypoint-web.sh
RUN chmod +x  $APP_HOME/entrypoint-celery.sh

RUN chown -R app:app $APP_HOME

USER app

RUN chmod +x /app/entrypoint-web.sh
RUN chmod +x /app/entrypoint-celery.sh
