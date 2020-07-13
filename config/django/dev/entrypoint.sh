#!/bin/sh

# install all dependencies
#pip install -r requirements.txt


# wait for Postgres to start
#function postgres_ready() {
#python << END
#import sys
#import psycopg2
#from decouple import AutoConfig

#config = AutoConfig(search_path='/opt/services/djangoapp')
#print config('SQL_DATABASE')
#print config('SQL_USER')
#print config('SQL_PASSWORD')
#print config('SQL_HOST')
#try:
#    conn = psycopg2.connect(
#        dbname=config('SQL_DATABASE'),
#        user=config('SQL_USER'),
#        password=config('SQL_PASSWORD'),
#        host="config('SQL_HOST')"
#    )
#except psycopg2.OperationalError:
#    sys.exit(-1)
#sys.exit(0)
#END
#}

#until postgres_ready; do
#  >&2 echo "Postgres is unavailable - sleeping"
#  sleep 1
#done

#echo "PostgreSQL started"

# Support sleep for container postgres is up
if [ "$DATABASE" = "dev" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Support sleep for containers elastic search is up
#while ! curl -X GET python_learning_es01:9200/_cluster/health --silent;
#  do
#    sleep 1
#  done

echo "Elastic Search 01 started"

#while ! curl -X GET python_learning_es02:9200/_cluster/health --silent;
#  do
#    sleep 1
#  done

echo "Elastic Search 02 started"


# Clear all database
#python manage.py flush --no-input

# Generate change for structure in database
python manage.py makemigrations
python manage.py migrate

# Create search index into elastic search
python manage.py search_index --create -f --parallel

# Sync data search index into elastic search
python manage.py search_index --populate -f

# Copy files static for folder in volume shared by container nginx
python manage.py collectstatic --no-input

# Changed function deprecate from django in django rest swagger load tag (staticfiles to static)
sed -i 's/load staticfiles/load static/' /usr/local/lib/python3.8/site-packages/rest_framework_swagger/templates/rest_framework_swagger/index.html

exec "$@"
