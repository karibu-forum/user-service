# base image
FROM python:3.7.2-alpine

# install dependencies
RUN \
    apk add --no-cache bash postgresql-client && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

RUN pip3 install pipenv

# set working directory
WORKDIR /home/app

COPY Pipfile Pipfile.lock ./

RUN apk add libffi-dev

RUN pipenv install --system --dev

RUN apk del build-deps

COPY ./entrypoint.sh /home/app/entrypoint.sh
RUN chmod 755 /home/app/entrypoint.sh

# add app
COPY . /home/app

# run server
CMD ["/home/app/entrypoint.sh"]
