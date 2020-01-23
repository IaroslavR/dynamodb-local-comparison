# Based on https://github.com/Countingup/docker-dynalite/blob/master/Dockerfile

FROM node:12-alpine

RUN addgroup dynalite && adduser -H -D -G dynalite dynalite

ARG DYNALITE_VERSION

# see https://github.com/npm/npm/issues/17851 for npm permissions issues when
# installing global packages as root, --unsafe-perm resolves this
# hadolint ignore=DL3018
RUN apk add --no-cache g++ make python \
    && npm install -g --unsafe-perm --build-from-source dynalite@~${DYNALITE_VERSION} \
    && apk --purge -v del g++ make python

USER dynalite

EXPOSE 8000

ENTRYPOINT ["dynalite", "--createTableMs", "0", "--deleteTableMs", "0", "--updateTableMs", "0", "--port", "8000"]