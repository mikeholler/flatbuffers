#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROD_REPOSITORY="https://upload.pypi.org/legacy"
TEST_REPOSITORY="https://test.pypi.org/legacy/"

twine upload \
    --username mikeholler \
    --password "$PYPI_PASSWORD" \
    --repository-url "$TEST_REPOSITORY" \
    "$DIR/../python/dist/"*

