FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  && apk add --no-cache git\
  && pip install pipenv

RUN mkdir /code
WORKDIR /code

# Install dependencys
ADD Pipfile /code/
ADD Pipfile.lock /code/
RUN pipenv install

# Copy src
COPY . /code/

EXPOSE 5000

CMD ["pipenv", "run", "flask", "run", "-h", "0.0.0.0"]

