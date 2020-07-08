#!/bin/sh

if [ "$DATABASE" = "dev" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Clear all database
#python manage.py flush --no-input

# install all dependencies
#pip install -r requirements.txt

# Generate change for structure in database
python manage.py makemigrations
python manage.py migrate

# Copy files static for folder in volume shared by container nginx
python manage.py collectstatic --no-input

exec "$@"
