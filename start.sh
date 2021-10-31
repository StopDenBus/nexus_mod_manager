#!/bin/bash

WORKING_DIR=$(dirname $0)

cd ${WORKING_DIR}

poetry run python3 "${WORKING_DIR}/app/__init__.py" $@