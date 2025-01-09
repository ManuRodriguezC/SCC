FROM python:3.8-alpine

WORKDIR /usr/app

RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev libc-dev \
    && pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]