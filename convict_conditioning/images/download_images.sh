#!/usr/bin/env bash

URL=$1
wget -i `wget -qO- ${URL} | sed -n '/<td/s/.*href="\([^"]*\)".*/\1/p'``]"'`
