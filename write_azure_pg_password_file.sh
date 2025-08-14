#!/usr/bin/env bash

set -e

curl -H "x-identity-header: ${IDENTITY_HEADER}" "${IDENTITY_ENDPOINT}?resource=https://ossrdbms-aad.database.windows.net&api-version=2019-08-01" \
  | jq -r .access_token \
  | awk '{print "*:*:*:*:"$1}' > ~/.pgpass \
&& chmod 600 ~/.pgpass
