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

<br />
# Snapshot of Travis CI Log Building and Testing Code

![image](https://user-images.githubusercontent.com/17459855/114327081-91e86380-9b05-11eb-8b84-2aed6a97fed8.png)

<br />

# Generated Logs when Containerizing Application

![image](https://user-images.githubusercontent.com/17459855/114327095-9f9de900-9b05-11eb-9d53-a7ad540ec965.png)

<br />

# Snapshot of Codecov.io Report of Code

![image](https://user-images.githubusercontent.com/17459855/114327106-aaf11480-9b05-11eb-8eaf-efaf02034535.png)

<br />

# Screenshot of Index.html on AWS Elastic Beanstalk along with URL box of browser

![image](https://user-images.githubusercontent.com/17459855/114329289-f0fda680-9b0c-11eb-93fb-ba17cc1abf68.png)

![image](https://user-images.githubusercontent.com/17459855/114329295-f4912d80-9b0c-11eb-998e-661df8365f00.png)

![image](https://user-images.githubusercontent.com/17459855/114329302-f8bd4b00-9b0c-11eb-883d-e94f81f9752c.png)

![image](https://user-images.githubusercontent.com/17459855/114329308-fd81ff00-9b0c-11eb-901d-e688122d67fe.png)

![image](https://user-images.githubusercontent.com/17459855/114329314-01ae1c80-9b0d-11eb-8e22-e0b0e52c9d4d.png)

![image](https://user-images.githubusercontent.com/17459855/114329323-0672d080-9b0d-11eb-96bd-0da644199a50.png)

![image](https://user-images.githubusercontent.com/17459855/114329332-0b378480-9b0d-11eb-8db0-e23b85d299d8.png)

![image](https://user-images.githubusercontent.com/17459855/114329357-1be7fa80-9b0d-11eb-95fd-f5a909c4276e.png)

<br />

# Snapshot of Ubuntu VM Desktop within Host Machine

![image](https://user-images.githubusercontent.com/17459855/114329381-2dc99d80-9b0d-11eb-95bb-2de0fcabf018.png)

![image](https://user-images.githubusercontent.com/17459855/114329387-315d2480-9b0d-11eb-8cb4-a7fc0889402a.png)

<br />

# AWS Lambda Function reading in and outputting JSON

![image](https://user-images.githubusercontent.com/17459855/114329407-40dc6d80-9b0d-11eb-9ba2-ee6f4d856bcb.png)

![image](https://user-images.githubusercontent.com/17459855/114329419-46d24e80-9b0d-11eb-8ba9-4c4fcd68d341.png)

![image](https://user-images.githubusercontent.com/17459855/114329422-49cd3f00-9b0d-11eb-9bff-c4264690bf00.png)







