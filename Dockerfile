FROM python:3

WORKDIR /app

COPY . .

RUN pip install aiogram

CMD [ "python", "./main.py" ]