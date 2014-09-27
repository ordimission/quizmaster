quizmaster
==========

Quizmaster is a python+javascript based quiz engine that requires a NoSQL database and access it with REST API architecture style.

* Requirements :
** clone Git
mkdir quizmaster
cd quizmaster
mkdir src
cd src
git clone https://github.com/ordimission/quizmaster.git

** import Database mongoDB
apt-get install mongodb
cd db
chmod +x import_mongo.sh
./import_mongo.sh

** Python environment
apt-get install python python-dev python-setuptools python-docutils python-virtualenv

cd ../..
virtualenv .
. bin/activate
pip install -r requirements.txt

* Runtime
** Run server
cd src
python main.py

** Launch client in browser
set URL to http://localhost:5001/quizmaster