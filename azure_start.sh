#!/usr/bin/env bash

set -e

./write_azure_pg_password_file.sh
nohup bash -c './periodically_write_azure_pg_password_file.sh | logger' &

/app/backend/start.sh
