#!/bin/sh
echo "Running Celery with autoreload"
CELERY_CMD="celery -A user_service.app.worker worker -l info -c1 -Q default --without-mingle --without-gossip --without-heartbeat"
$CELERY_CMD
