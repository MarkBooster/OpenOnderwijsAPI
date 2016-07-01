Getting started with Open OnderwijsAPI
======================================

## Prerequisites

 * Python (2.7)
 * python-virtualenv [Install python-virtualenv](/doc/installation/python-virtualenv.md)

## Installation

The API is implemented using Python and the Django REST framework.  To get
started, follow these steps to create a self-contained, fully functional reference API:

### Step 1: Clone repository

    git clone https://github.com/OpenOnderwijsAPI/OpenOnderwijsAPI.git

    cd OpenOnderwijsAPI

### Step 2: Setup python environment

    virtualenv env

    source env/bin/activate

### Step 3: Install python modules

    pip install -r requirements.txt

### Step 4: Setup database

    python manage.py migrate

    python manage.py loaddata ./api/fixtures/*

**When asked create a superuser**

### Step 5: Start the local server

    python manage.py runserver

## Usage

At that point, you should be able to browse to http://localhost:8000/. This should show an overview of the available
APIs. A somewhat more extensive API description can be found at http://localhost:8000/docs

## Deployment

Before deploying to production, you should dump all static assets:

    python manage.py collectstatic

## Next Steps

* [Enable OAuth2 Authentication](/doc/installation/oauth2.md)
* [Enable Search](/doc/installation/search.md)
