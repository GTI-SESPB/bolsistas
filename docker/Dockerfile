FROM python:3.11-bookworm AS instalador

ENV DEBIAN_FRONTEND="noninteractive" \
    TZ="America/Sao_Paulo" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install -r requirements.txt gunicorn


FROM python:3.11-slim-bookworm

RUN apt-get update &&\
    apt-get install -y libpq5

WORKDIR /app

COPY --from=instalador /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .

ENTRYPOINT ["sh", "start.sh"]
