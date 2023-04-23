#!/bin/sh
echo Setup Development Container
echo ==============================

echo ... Installing linux packages
sudo apk add py3-pip

echo ... Create and Activate virtual environment
ls -a
sudo rm -r -f .venv
sudo python -m venv .venv
source .venv/bin/activate

echo ... Installing python packages
sudo pip install --upgrade pip
pip install -r requirements.txt
# pip freeze > requirements.txt

echo Python environment libraries: 
pip list

echo Done!
echo =============================