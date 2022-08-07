# Django CRUD with MySQL that uses Django Rest Framework for building Rest APIs
## Architecture: 
- HTTP requests will be matched by Url Patterns and passed to the Views
- Views processes the HTTP requests and returns HTTP responses (with the help of Serializer)
- Serializer serializes/deserializes data model objects
- Models contains essential fields and behaviors for CRUD Operations with MySQL Database

## Technologies: 
- Python
- Django 
- Django Rest Framework 
- PyMySQL 
- django-cors-headers 

## Project Structure: 

- EmployeeApp/apps.py: declares TutorialsConfig class (subclass of django.apps.AppConfig) that represents Rest CRUD Apis app and its configuration.
- DjangoAPI/settings.py: contains settings for our Django project: MySQL Database engine, INSTALLED_APPS list with Django REST framework, Tutorials Application, CORS and MIDDLEWARE.
EmployeeApp/models.py: defines Employees and Deprtment data models class (subclass of django.db.models.Model).
- migrations/0001_initial.py: is created when we make migrations for the data model, and will be used for generating MySQL database table.
- EmployeeApp/serializers.py: manages serialization and deserialization with EmployeeAppSerializer class (subclass of rest_framework.serializers.ModelSerializer).
- EmployeeApp/views.py: contains functions to process HTTP requests and produce HTTP responses (using EmployeeAppSerializer).
- EmployeeApp/urls.py: defines URL patterns along with request functions in the Views.
- EmployeeApp/urls.py: also has URL patterns that includes tutorials.urls, it is the root URL configurations.
Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in email.

## Dockerize the application: 

**Dockerfile**
Create a Dockerfile under your djangomysql directory with the following content.
```sh
FROM python:3.8
ENV PYTHONUNBUFFERED 1 
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . . 
```

**requirements.txt**
The file, requirements.txt, is generally created under the directory djangomysql to declare what all Python packages you need to install in the container. Here I am installing Django and django-mysql.
```sh
django
djangorestframework
django-cors-headers
mysqlclient 
sqlparse
pytz
asgiref
psycopg2-binary
```
**Docker Compose**
```yaml
version: "3.8"
services: 
  app: 
    build: .
    volumes: 
      - .:/app/
    expose:
      - 8000
    ports:
      - "8000:8000"
    container_name: app
    command: ["python3", "app/manage.py", "runserver", "0.0.0.0:8000"]
    depends_on:
      - db
  db: 
    image: mysql:5.7
    volumes:
        - ./data/mysql/db:/var/lib/mysql
    ports: 
        - "3306:3306" 
    environment:
      MYSQL_DATABASE: 'employees'
      MYSQL_ALLOW_EMPTY_PASSWORD: 'true'
    container_name: db
```
**Build and run the application**
```sh
docker-compose up --build
docker exec -d app /bin/bash python3 app/manage.py migrate

# push the image to docker up
docker login
docker tag "username"/"image-name":"tag"
docker push "image-name"
```

-----------------------------------------------------------------------------------

## Creating Helm Chart: 

**Create a helm chart**
```sh
mkdir helm && cd helm
helm create django-api
```

**Add the dependency in Chart.yaml**

```yaml
dependencies:
  - name: mysql
    version: "8.8.6"
    repository: "@bitnami"
```

**Update the dependency**
```sh
helm dependency update
```

**Add the mysql configuration in Values.yaml**
```yaml
mysql: 
  auth: 
    rootPasswor: password
    database: employees
  primary: 
    service: 
      type: NodePort
      nodePort: 32762
  fullnameOverride: db
  initdbScriptsConfigMap: mysql-initdb-config
```

**Update the template files with the app configurations. Then install the chart**
```sh
helm install django-app .
```

**Verify the installations**

```sh
kubectl get pods 
kubectl get svc
```