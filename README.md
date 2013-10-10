Demo-AngelList
==============

Demo project with AngelList data

Setup Django Backend
=====================

Setup virtualenv for this project
----------------------------------

Install Python virtualenv if you don't have it. It’s highly recommended (although not required) to use virtualenv so that the python project setup won't conflict with others.

	$ pip install virtualenv

Create virtualenv for angellist_demo

	$ cd backend/
	$ virtualenv angellist_demo_env

Activate the virtualenv

	$ source angellist_demo_env/bin/activate

You should notice that the Python and Pypi inside angellist_demo_env are being used now:

	$ which python
	$ which pypi

Install [Django MongoDB Engine](http://django-mongodb-engine.readthedocs.org/en/latest/index.html)

	$ pip install git+https://github.com/django-nonrel/django@nonrel-1.3
	$ pip install git+https://github.com/django-nonrel/djangotoolbox@toolbox-1.3
	$ pip install git+https://github.com/django-nonrel/mongodb-engine@mongodb-engine-1.3

Install [Django Rest Framework](http://django-rest-framework.org/)

	$ pip install djangorestframework
	$ pip install markdown
	$ pip install django-filter


Import data into MongoDB for Django
------------------------------------

	$ cd backend/angellist_demo
	$ python manage.py shell
	>>> execfile('batch_import_django.py')


Start Django
=============

Activate the virtualenv if it is not activated yet

	$ cd backend
	$ source angellist_demo_env/bin/activate

Start Django

	$ cd ../angellist_demo
	$ python manage.py runserver [::]:8000

