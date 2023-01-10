# Simple chat on Django/React with Pusher


Start
-----

Create file `.env` or delete `.example` in the `.env.example` file

Fill in the data in the file `.env`

#### [Keys](https://pusher.com/) for pusher

`.env`

```dotenv
# Django/Python
SECRET_KEY=KEY
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1,etc...

# Pusher/Backend
APP_ID=app_id
KEY=key
SECRET=secret
CLUSTER=cluster
SSL=1
```

`frontend/.env`

```dotenv
# Pusher/Frontend
REACT_APP_APP_KEY=key
REACT_APP_CLUSTER=cluster
```

Run
---

```
docker-compose up
```

### Standard ports

* [Backend](http://localhost:8000/): 8000
* [Frontend](http://localhost:3001/): 3001
