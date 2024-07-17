FROM python:3.11.2-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


WORKDIR /usr/src/app/

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

COPY . /usr/src/app/

CMD ["python", "./app/bot.py"]