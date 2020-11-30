# MukaiGuy Website Documentation

Jump to:
- [MukaiGuy Website Documentation](#mukaiguy-website-documentation)
  - [The Backend](#the-backend)
  - [The Frontend](#the-frontend)
  - [The Database](#the-database)
  - [The Containerization](#the-containerization)


## [The Backend](#backend)
<p>The server side backend is built around the django web framework.</p>

<ul> Using pip install the following


- [ ] Django = django
- [ ] Django-REST-Framework = djangorestframework
- [ ] Postgres = psycopg2-binary
- [ ] Pytest = pytest pytest-django
- [ ] dajngo-webpack-loader
- [ ]
- [ ]
- [ ]
</ul>

## [The Frontend](#frontend)
<p>The client side frontend is built around the ReactJS framework.</p>

<ul> Using `Yard add <package>` or `npm install <package> --save-dev`

- [ ] create react-app
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
</ul>

## [The Database](#database)
Currently the database is setup to use PostgresQL via a docker container

>DATABASE=mukaiguy_dev
>USER=mukaiguy
>Dev PASSWORD=4BJX*n&x5c4pWdt
>HOST=mukaiguy-db
>PORT=5432
>DATABASE=postgres

To ensure that the database can communicate with the container we will create a file called `entrypoint.sh`
Enterypoint.sh will contain the following. Notice the first line after the `!#bin/sh` contains`[ "$DATABASE" = "postgres" ]` this is what the last line from the above variables is refering to. I would assume that you should probably change that to what ever database you are going to use. After you create your **entrypoint.sh** file you'll need to make it [exacutable](#exacutable) 


> ## The entrypoint.sh file

```sh
#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"
```

> ## To make it [Exacutable](#exacutable)

```sh
chmod +x entrypoint.sh 

# Make sure your in the same directory as the entrypoint.sh file.
```


## [The Containerization](#container)

For this project we are using Apline Linux as the base. 