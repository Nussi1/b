FROM python:3.10

WORKDIR /advertisement

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD . /advertisement

COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt



CMD python manage.py makemigrations && python manage.py migrate
COPY . /