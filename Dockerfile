FROM python:3.9.2-alpine

EXPOSE 8080

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY app app


CMD ["gunicorn", "--workers=2", "-b", "0.0.0.0:8080", "app.src.main:app", "&" ]

# run with docker build -t test
# docker run -it -p 8080:8080 test