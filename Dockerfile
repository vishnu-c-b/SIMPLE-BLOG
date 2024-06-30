
FROM python:3.12.3-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /code


RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /code/
RUN pip install  -r requirements.txt


COPY . /code/

RUN python manage.py makemigrations
RUN python manage.py migrate



EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]