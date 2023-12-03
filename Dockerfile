FROM python:3.12

WORKDIR /app

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

COPY . .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000