CRUD Products
===============

Requierements
-------------
* python 3.7 or higher
* django
* django-rest-framework
* psycopg2

Prepare
-------------

First, you need to prepare database for this app. I guess you know, how to create new database in Shell-console.
Name of Database should be "Products". 

When a database is created, clone this repo by method, which is comfortable for you also you have to make a new .sh file describing environment variables. Enter command:

.. code-block::

    touch setenv.sh

Fill setenv.sh file the following content:

.. code-block::
    
    export DATABASE_NAME="name of your databes(I recommend products)"
    export DATABASE_USER="user name"
    export DATABASE_PASS="password"
    export DATABASE_HOST="host"
    export DATABASE_PORT="port"
    export SECRET_KEY="SECRET_KEY Django project"

I hope you've created database and setenv.sh file. It is so neccessary for correct work.

.. code-block::
    source ./setenv.sh


