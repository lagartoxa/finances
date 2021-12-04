#!/bin/bash

echo "Looking for old venv"
if [ -d "./backend/venv" ]
then
    echo "Old venv found. Removing it..."
    rm -rf ./backend/venv
    echo "Old venv deleted successfully!"
else
    echo "Old venv not found. Skipping removal..."
fi

echo "Creating venv"
python3 -m venv ./backend/venv
echo "New venv created successfully!"

