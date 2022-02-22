FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG USER_ID=1000
ARG GROUP_ID=1000

# обновляем систему
RUN apt-get update && apt-get upgrade -y

#marketbackend <-- Юзер
RUN groupadd -g ${GROUP_ID} marketbackend &&\
    useradd -l -u ${USER_ID}  -g marketbackend marketbackend &&\
    install -d -m 0755 -o marketbackend -g marketbackend /home/marketbackend &&\
    chown --changes --silent --no-dereference --recursive \
    --from=33:33 ${USER_ID}:${GROUP_ID} \
    /home/marketbackend

# Переместиться сюда для создания в этой dir новые дирректории
WORKDIR /home/marketbackend

# Создать дирректорию с кодом.
RUN mkdir -p src/app

# Поменять везде права на обычного юзера
RUN chown -R marketbackend:marketbackend .

USER marketbackend

# Создать дирректории
RUN mkdir -p vol/web/static
RUN mkdir -p vol/web/media
RUN chmod -R 755 vol/web

WORKDIR src/app

COPY --chown=marketbackend:marketbackend ./requirements.txt .

RUN pip install --user --upgrade pip

RUN pip install --user -r requirements.txt

ENV PATH="${HOME}/.local/bin:${PATH}"

# Копировать код
COPY --chown=marketbackend:marketbackend marketplace/ src/app

# Запуск дев. среда
CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']
