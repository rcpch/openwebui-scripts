#!/usr/bin/env bash

set -e

while true;
do
  ./write_azure_pg_password_file.sh
  sleep 10s
done
