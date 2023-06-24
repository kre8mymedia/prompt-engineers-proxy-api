#!/bin/sh

set -a # automatically export all variables
source .env
set +a

uvicorn main:app --port $PORT --reload --log-level debug