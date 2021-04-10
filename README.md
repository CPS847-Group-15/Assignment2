# Assignment2
[![Build Status](https://travis-ci.com/CPS847-Group-15/Assignment2.svg?branch=main)](https://travis-ci.com/CPS847-Group-15/Assignment2)

For our assignment 2, we've created a simple web application which
generates a simple index.html displaying "Hello World!". It can
also tell a joke at the path `/joke`, and can play fizzbuzz at the
path `/fizzbuzz?number=<number>`.

## Instructions
This program can either be run directly, in which case main.py will use
a simple HTTP server, or it can be run from a Docker container, which 
will serve it using Gunicorn.

Use the following commands to run it with Docker:
```bash
$ docker build -t Assignment2 .
$ docker run -it -p 8080:8080 Assignment2
```
