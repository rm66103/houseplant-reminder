# houseplant-reminder
did I water my houseplants?

## What is this project?
This project is a solution to the problem of forgetting to water your houseplants.

In addition to providing forgetful plant parents with SMS reminders to care for their leafy loved ones,
it is my goal to document my development process on a personal project, implement Celery, and write efficient & well
tested code.

Users will receive a text message each day that specifies which of their plants need to be watered. The user will be provided a link which they will be instructed to visit when they water their plants. 

## Concerns

**Cost** - To minimize cost, an account should receive 1 text reminder each day with all of the reminders for that day.

**Tech** - To schedule jobs, we will use [Celery](https://docs.celeryq.dev/en/stable/index.html). For SMS we will use the Twilio API or library.

## Support Guide

### Creating a user
TODO

## Dev Guide

### Setup

Configure a development environment for python 3.9.1 with pyenv.

Install the libraries.
```
pip install -r requirements.txt
```

Create a file called `.env` in the same directory as `.env.template`. Copy and paste `.env.template` into `.env` and then set your environment variables.

### Running specs

```
python manage.py test
```

The project is configured to output a coverage report to the `coverage` directory. It is created if it does not exist, and the coverage reports are not tracked in Git.