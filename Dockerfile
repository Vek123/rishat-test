FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements/prod.txt

WORKDIR /app/store

RUN python manage.py collectstatic

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "store.wsgi:application"]
