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
$ docker build -t assignment2 .
$ docker run -it -p 8080:8080 assignment2
```

# Snapshot of Travis CI Log Building and Testing Code

![image](https://user-images.githubusercontent.com/17459855/114327081-91e86380-9b05-11eb-8b84-2aed6a97fed8.png)


# Generated Logs when Containerizing Application

![image](https://user-images.githubusercontent.com/17459855/114327095-9f9de900-9b05-11eb-9d53-a7ad540ec965.png)


# Snapshot of Codecov.io Report of Code

![image](https://user-images.githubusercontent.com/17459855/114327106-aaf11480-9b05-11eb-8eaf-efaf02034535.png)
