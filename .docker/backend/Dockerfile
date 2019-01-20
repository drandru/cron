FROM registry.mos-team.ru/mosru/php:7.1-base

COPY --chown=docker:docker .deploy/docker/backend/entrypoint.sh /entrypoint.sh

# Copy project
COPY --chown=docker:docker . /app

RUN chown docker:docker /app

WORKDIR /app/backend

USER docker:docker
