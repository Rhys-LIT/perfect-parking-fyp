# Django Command History

## Create Website Project

```bash
django-admin startproject PerfectParkingWebsite
```

## Create App

```bash
python manage.py startapp PerfectParking
```

## Create Superuser

```bash
python manage.py createsuperuser
```

## Migration


```bash
python manage.py makemigrations PerfectParking
```

```bash
python manage.py sqlmigrate PerfectParking 0001
```

> Note `0001` is the migration number. This number will increment with each migration. Adjust the number accordingly to the latest migration.
Migrations can be found in the [migrations](../PerfectParking/migrations/) folder.

```bash
python manage.py migrate
```

## Run Server

```bash
python manage.py runserver
```

[https://docs.djangoproject.com/en/4.1/intro/tutorial01/](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)

## Django Rest Command History

### Install Django Rest Framework

#### Pip

```bash
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

#### Conda

```bash
conda install -c conda-forge djangorestframework
conda install -c conda-forge markdown
conda install -c conda-forge django-filter
```

### 