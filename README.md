# gif_library
### Python API for giphy library using [Flask](http://flask.palletsprojects.com/en/1.1.x/) and [Mongodb](https://docs.mongodb.com/manual/).
Resources for users and gifs available.  Resources for users allow for creation, retreival, update, login, logout. For gifs search is available.  JWT is used for authentication and is set using an 'httponly' cookie and protected with a CSRF token. Bcrypt is used for password hashing and validation. Docker is used to set up a development environment.

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

```CORS_ORIGIN_WHITELIST = ["at least need 'http://localhost:3000' for dev]```


## Set up
### Install docker along with docker-compose

From the project directory execute:

```docker-compose build```

```docker-compose up```

### Some notes on improvements to be made with more time:

- Add JWT refresh tokens and lower the time to live for tokens
- Complete unit testing
- Logging
- Doc strings
