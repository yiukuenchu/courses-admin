**SL-101**

**Title:** Manage Courses and Intakes with API Endpoint

**Description:**

As an Admin user,
I want to have the ability to create and manage courses and their associated intakes within the Django Admin interface,
so that I can efficiently organize and update course offerings.

Additionally, I need an API endpoint that provides a list of all available courses along with their respective intakes,
so that this data can be accessed programmatically for integration with other systems or for front-end display.

**Acceptance Criteria:**

- [x] A course has a unique `id` and a `name`
- [x] An intake has a unique `id`, a `start_date`, and an `end_date`
- [x] A course can have multiple intakes associated with it
- [x] Ability to create/manage courses within the Django Admin interface
- [x] Ability to create/manage intakes within the Django Admin interface
- [x] `/api/admissions/courses/` API endpoint that provides a list of all available courses along with their respective intakes
- [x] Access to this endpoint has to be authenticated using [DRF token](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)
- [x] Unit tests to make sure the endpoint behaves as intended

If you have any ideas for enhancing your implementation but don't have the time or aren't sure how to achieve them in Django, don't worry.
You're encouraged to note them as comments in the code or in a separate document.

**Getting Started**

Please use the boilerplate code provided as a starting point. The code has 3 parts:

- `apps/admission/` - this is where you'll define the models and the associated Django admins
- `apps/api/` - this is where you'll define the DRF view, serializers, and relevant unit tests
- `config/` - this is where you'll find the project's settings and URL conf

**With Docker**

- Install docker https://docs.docker.com/engine/install/
- Install docker compose https://docs.docker.com/compose/install/
- Build docker image and start the container:

```shell
docker compose up
```

- Run unit tests:

```shell
docker compose run --rm django pytest
```

**Without Docker**

- Install pipenv https://pipenv.pypa.io/en/latest/installation.html
- Install dependencies:

```shell
pipenv install --deploy --dev
```

- Apply migrations:

```shell
pipenv run ./manage.py migrate
```

- Create an account for Django admin interface:

```shell
pipenv run ./manage.py createsuperuser
```

- Run the application:

```shell
pipenv run ./manage.py runserver 0.0.0.0:8000
```

- Run unit tests:

```shell
pipenv run pytest
```

## In a browser

- Open http://0.0.0.0:8000/admin/
- Login to Django admin interface with the account created
- View/Add a course
- View/Add an intake
- View Auth token

## In Postman

### 1. POST Auth Token

- http://0.0.0.0:8000/api-token-auth/
- POST request
- Body:
  - use 'x-www-form-urlencoded' format
  - username: YOUR_USERNAME
  - password: YOUR_PASSWORD
- Send request
- Copy the token

### 2. GET Courses

- http://0.0.0.0:8000/api/admissions/courses/
- GET request
- Header:
  - Authorization: Token YOUR_AUTH_TOKEN
- Send request
