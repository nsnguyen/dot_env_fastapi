
FROM python:3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
 
COPY . .

# WORKDIR /app

EXPOSE 8002

CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8002"]


# CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]