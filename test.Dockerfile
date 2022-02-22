FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG USER_ID=1000
ARG GROUP_ID=1000

RUN pip3 install pipenv


# Перемещаюсь сюда для создания в этой dir новые папки
WORKDIR /src/app

COPY marketplace/ ./

RUN pipenv install --system --deploy --ignore-pipfile

RUN useradd -m myapp
USER myapp
