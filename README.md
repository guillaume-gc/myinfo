# myinfo
With MyInfo, get your personal info and edit them!

# How to use

- Clone the directory.
- Create a python environement (version 3.8.5 recommanded) with listed python packages (see detailed guide).
- Add secret information (see detailed guide).
- Start server: `python manage.py runserver 8000` (within the project root directory).

The project should use the following URL by default:
```
http://127.0.0.1:8000/
```

# Detailed Guide

## Python packages

List of used Python packages used (probably need to clean it up):

```
Django asgiref certifi chardet coverage coveralls defusedxml django-allauth django-nose djangorestframework docopt gunicorn idna mysqlclient nose oauthlib pip python3-openid pytz requests requests-oauthlib setuptools sqlparse urllib3 whitenoise
```

Detailed list, in case there is a version issue:
```
PACKAGE VERSION
Django	3.0.8
asgiref	3.2.10
certifi	2020.6.20
chardet	3.0.4
coverage	5.2.1
coveralls	2.1.1
defusedxml	0.6.0
django-allauth	0.42.0
django-nose	1.4.6
djangorestframework	3.11.0
docopt	0.6.2	
gunicorn	20.0.4
idna	2.10
mysqlclient	2.0.1
nose	1.3.7
oauthlib	3.1.0
pip	20.1.1
python3-openid	3.2.0
pytz	2020.1
requests	2.24.0
requests-oauthlib	1.3.0
setuptools	49.2.0
sqlparse	0.3.1
urllib3	1.25.10
whitenoise	5.1.0
```

## Secret

### Database

database/mariadb.cnf and database/reset_users

(optional) change the password for myinfo user, default password is `myinfo`.

### Django Settings

Execute the following command, within the projet root directory:
```
python manage.py shell -c "from django.core.management import utils; print(utils.get_random_secret_key())"
```

Copy the generated secret key (for example : `nyq*sfbt0c)(1fg8$^%#db3wd3451*=nz-h@nbi++fs-wm^%-4`).

Find the following line in myinfo/settings.py:
```
SECRET_KEY = 'SECRET_KEY'
```
Past the generated key. Example:
```
SECRET_KEY = 'nyq*sfbt0c)(1fg8$^%#db3wd3451*=nz-h@nbi++fs-wm^%-4'
```
