FROM ubuntu:latest

COPY .deploy/docker/cron/shedule.cron /etc/cron.d/sample

RUN apt-get -qq update && \
    apt upgrade -y && \
    apt install -y \
        cron \
        rsyslog \
        python &&\
    chmod 0755 /etc/cron.d/sample

COPY /cron /app/cron

WORKDIR /app/cron

CMD service rsyslog start && service cron start && tail -f /var/log/syslog
