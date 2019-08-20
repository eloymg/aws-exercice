#!/bin/bash

yum install -y python3
yum install -y git

git clone https://github.com/eloymg/aws-exercice
pip3 install -r aws-exercice/requirements.txt
python3 aws-exercice/app.py &