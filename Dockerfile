FROM python:3-slim AS build-env

COPY . /app
WORKDIR /app


FROM gcr.io/distroless/python3

# Копирует pip и список зависимостей для установки
COPY --from=build-env /app/get-pip.py app/requirements.txt ./app/
WORKDIR /app

RUN python get-pip.py
RUN pip install --no-cache-dir -r requirements.txt

# Копирует исходый код
COPY --from=build-env /app .

CMD ["main.py"]