# News Articles Backend System

## Introduction

This is a Django based back-end system and API that displays a list of news articles. Each article has the following fields: Title, summary, content (HTML), published (yes/no), and published date. Each article belongs to a news category and has an author. Each author has the following fields: name, surname, and job description.

The system includes an admin panel that can be used to store and update the information and REST API endpoints for retrieving news categories, authors, and news articles.

## Requirements

Before setting up the project, make sure you have the following installed:

- Python 3.x
- Poetry (Optional)
- Docker (Optional)

## Setup

### Option 1: Using Poetry

1. Navigate to the project directory: `cd cocoon-news-project`
2. Create a virtual environment: `poetry install`
3. Activate the virtual environment: `poetry shell`
4. Install the dependencies: `poetry install`
5. Migrate the database: `python manage.py migrate`
6. Run the development server: `python manage.py runserver`

## Option 2: Using Docker

1. Navigate to the project directory: `cd cocoon-news-project`
2. Build the Docker image: `docker compose build`
3. Run a Docker container: `docker compose up`

## Running the Tests

To run the tests, run the following command: `pytest`

## Admin Panel

To access the admin panel, navigate to <http://localhost:8000/admin> in your web browser. Use the following credentials to log in:

- username: admin
- password: admin

## Admin Dashboard

To access the admin panel, navigate to <http://localhost:8000/> in your web browser. Where you should be able to see articles created, create new articles and update existing articles:

## REST API Endpoints

- News Categories: `http://localhost:8000/api/v1/news/category/`
- Authors: `http://localhost:8000/api/v1/author/`
- News Articles: `http://localhost:8000/api/v1/news/articles/`

### Swagger Docs

To access the Swagger UI, navigate to <http://localhost:8000/api/schema/swagger-ui/>  in your web browser.

## Conclusion

This project provides a basic structure for a news articles back-end system using Django.
