FROM alpine:3.6

# hadolint ignore=DL3018
RUN apk add --no-cache --update \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    python3

WORKDIR /moto/

ENV PYTHONUNBUFFERED 1

ARG MOTO_VERSION

# hadolint ignore=DL3013
RUN  python3 -m ensurepip && \
     rm -r /usr/lib/python*/ensurepip && \
     pip3 --no-cache-dir install --upgrade pip setuptools && \
     pip3 --no-cache-dir install "moto[server]==${MOTO_VERSION}"

EXPOSE 8000

ENTRYPOINT ["/usr/bin/moto_server", "dynamodb", "-H", "0.0.0.0", "-p8000"]

