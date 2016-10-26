# Introduction
This django project is test work for steelkiwi. Follow the instructions for local deployment.
use python 3.5.2, MySQL server.
# Local deployment
To run this install requirements on your virtual environment
```
pip install -r requirements.txt
```
Change *my.cnf* settings(user, password, database) to local ones. Then migrate db
```
python manage.py migrate
```
Also you need to add superuser to add new objest Category and Product in DB. Also you may create new users in admin panel.
```
python manage.py createsuperuser
```
After that you can runserver with commands: 
```
python manage.py runserver --settings=kiwisite.settings.local
python manage.py runserver --settings=kiwisite.settings.deploy
```
default settings - kiwisite.settings.local, so just write
```
python manage.py runserver [options]
```
to work.
Check http://localhost:8000/ as common user or as admin(you have created previously). To see admin panel visit
http://localhost:8000/admin