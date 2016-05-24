# morepath_services
Demonstrate morepath_services integration with [Morepath](http://morepath.readthedocs.io).

## Getting started

```shell
$ git clone git@github.com:blaflamme/morepath_services.git
$ cd morepath_services
$ pyvenv .
$ source bin/activate
$ pip install -U -e .
```

Then initialize the database

```shell
$ init-database
```

Then run the default development WSGI server

```shell
$ run-demo
```

The application is now up at [http://localhost:5000](http://localhost:5000), or you can run the amazing `gunicorn` WSGI server

```shell
$ gunicorn --reload morepath_services.run
```

The application is now up at [http://localhost:8000](http://localhost:8000)
