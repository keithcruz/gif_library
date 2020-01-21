## gif_library
Python API for giphy library using Flask and Mongodb.

## Set up
### Created with python 3.7.6

```python -m venv env```

```pip install -r requirements.txt```


### Create the required environment variables

```export FLASK_APP=app.py```

```export ENV_FILE="path to .env file```


### .env file contents:

```MONGODB_DB="name of the db to use"```

```MONGODB_HOST="db hostname"```

```MONGODB_PORT="db port"```

```GIPHY_API_KEY="key to access the giphy api"```

```JWT_SECRET_KEY = "secret to use for jwt"```

```JWT_REFRESH_TOKEN_EXPIRES="int (seconds)"```

```JWT_ACCESS_TOKEN_EXPIRES="int (seconds)"```
