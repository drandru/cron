#!/bin/sh

# Stop on any error
set -e

# For local development only
if [ "${ENABLE_FIXUID:-0}" = "1" ]; then
  fixuid
fi

echo "Current user: $(whoami)"

echo "Configuring PHP settings from ENV variables"
echo "date.timezone = ${TIMEZONE}" >> ${PHP_SETTINGS}
echo "short_open_tag = ${PHP_SHORT_OPEN_TAG}" >> ${PHP_SETTINGS}
echo "display_errors = ${PHP_DISPLAY_ERRORS}" >> ${PHP_SETTINGS}
echo "log_errors = ${PHP_LOG_ERRORS}" >> ${PHP_SETTINGS}
echo "upload_max_filesize = ${PHP_UPLOAD_MAX_FILESIZE}" >> ${PHP_SETTINGS}
echo "post_max_size = ${PHP_POST_MAX_SIZE}" >> ${PHP_SETTINGS}
echo "memory_limit = ${PHP_MEMORY_LIMIT}" >> ${PHP_SETTINGS}

echo "Init app"
if [ ! -f /tmp/initialized ]; then
  #composer run-script auto-scripts

 # if [ ! "${APP_ENV}" = "dev" ]; then
 #   bin/console cache:warmup
  #fi

  touch /tmp/initialized
fi

echo "Start app"
exec php-fpm -O -F
