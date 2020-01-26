## gif_library
Python API for giphy library using Flask and Mongodb.


### .env file contents for development:

```MONGODB_DB="gif-library-dev"```

```MONGODB_HOST="flaskdb"```

```MONGODB_PORT=27017```

```GIPHY_API_KEY="key to access the giphy api"```

```JWT_SECRET_KEY = "secret to use for jwt"```

```JWT_ACCESS_TOKEN_EXPIRES="int (seconds)"```

```JWT_TOKEN_LOCATION=["cookies"]```

```JWT_COOKIE_SECURE="FALSE" (for dev, true in production)```

```JWT_ACCESS_COOKIE_PATH="paths to send jwt"```

```JWT_ACCESS_CSRF_COOKIE_PATH="paths to send csrf"```

```JWT_COOKIE_CSRF_PROTECT="TRUE"```

```JWT_CSRF_METHODS=["POST", "PUT", "PATCH", "DELETE", "GET"]```

```PROPOGATE_EXCEPTIONS="TRUE"```

```CORS_ORIGIN_WHITELIST = [ "at least need 'http://localhost:3000' for dev]```


## Set up
### Install docker along with docker-compose

From the project directory execute:

```docker-compose build```

```docker-compose up```
