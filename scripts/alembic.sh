#!/bin/bash

alembic -c backend/db/migrations/alembic.ini "${@}"

