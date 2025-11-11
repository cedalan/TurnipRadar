#!/bin/bash
set -e

#Create viritual environment since homebrew is kinda cool but i cannot get pip3 to work...
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

#Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

#Upgrade pip just in case
echo "Upgrading pip..."
pip install --upgrade pip

#Install requirements
if [ -f "requirements.txt" ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt
else
    echo "Could not fint requirements.txt..."
fi

#Start scraper
python scraper.py
