#!/bin/bash
set -e

echo "Running Django collectstatic..."
python3 manage.py collectstatic --noinput
