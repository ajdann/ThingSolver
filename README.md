# How to run dockerized app

Build docker image:

```
docker build --tag pythonapp .
```

Run docker image:

```
docker run -d -p 8000:8000 --name pythonappcon pythonapp
```
