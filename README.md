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

```JWT_TOKEN_LOCATION=["cookies"]```

```JWT_COOKIE_SECURE="FALSE" (for dev, true in production)```

```JWT_ACCESS_COOKIE_PATH="paths to send jwt"```

```JWT_ACCESS_CSRF_COOKIE_PATH="paths to send csrf"```

```JWT_REFRESH_COOKIE_PATH="paths to send reresh"```

```JWT_REFRESH_CSRF_COOKIE_PATH="paths to send reresh csrf"```

```JWT_COOKIE_CSRF_PROTECT="TRUE"```

```JWT_CSRF_METHODS=["POST", "PUT", "PATCH", "DELETE", "GET"]```

```PROPOGATE_EXCEPTIONS = "TRUE"```

```CORS_ORIGIN_WHITELIST = [ "at least need 'localhost:3000' for dev]```
