#!/usr/bin/env bash

set -e

echo 'Updating pgpass file'

curl --silent -H "x-identity-header: ${IDENTITY_HEADER}" "${IDENTITY_ENDPOINT}?resource=https://ossrdbms-aad.database.windows.net&api-version=2019-08-01" \
  | jq -r .access_token \
  | awk '{print "*:*:*:*:"$1}' > ~/.pgpass

chmod 600 ~/.pgpass

echo 'Updated pgpass file'
