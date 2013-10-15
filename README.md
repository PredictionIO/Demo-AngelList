Demo-AngelList
==============

Demo project with AngelList data

Setup Django Backend
=====================

Setup virtualenv for this project
----------------------------------

Install Python virtualenv if you don't have it. It’s highly recommended to use virtualenv so that this python project setup won't conflict with others.

	$ pip install virtualenv

Create virtualenv for angellist_demo

	$ cd backend/
	$ virtualenv angellist_demo_env

Activate the virtualenv

	$ source angellist_demo_env/bin/activate

You should notice that the **python** and **pip** inside angellist_demo_env are being used now:

	(angellist_demo_env)$ which python
	Demo-AngelList/backend/angellist_demo_env/bin/python
	(angellist_demo_env)$ which pip
	Demo-AngelList/backend/angellist_demo_env/bin/pip

Install [Django MongoDB Engine](http://django-mongodb-engine.readthedocs.org/en/latest/index.html):

	(angellist_demo_env)$ pip install git+https://github.com/django-nonrel/django@nonrel-1.3
	(angellist_demo_env)$ pip install git+https://github.com/django-nonrel/djangotoolbox@toolbox-1.3
	(angellist_demo_env)$ pip install git+https://github.com/django-nonrel/mongodb-engine@mongodb-engine-1.3

Install [Django Rest Framework](http://django-rest-framework.org/):

	(angellist_demo_env)$ pip install djangorestframework
	(angellist_demo_env)$ pip install markdown
	(angellist_demo_env)$ pip install django-filter


Import data into MongoDB for Django
------------------------------------

	(angellist_demo_env)$ cd backend/angellist_demo
	(angellist_demo_env)$ python manage.py shell
	>>> execfile('batch_import_django.py')


Start Django
=============

Activate the virtualenv (if it is not activated yet)
-----------------------------------------------------
	
	$ source backend/angellist_demo_env/bin/activate

Start Django
-------------

	(angellist_demo_env)$ cd backend/angellist_demo
	(angellist_demo_env)$ python manage.py runserver [::]:8000

Simple test 
------------

	$ curl localhost:8000/startups.json -H 'Accept: application/json' 
	$ curl localhost:8000/startups/190752.json -H 'Accept: application/json' 
