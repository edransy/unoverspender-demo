![Test Image 4](https://imgur.com/o8yBGIp.png)

# Dockerizing Flask with Postgres

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx).

## Want to use this project?

### Development

Uses the default Flask development server.

1. Rename _.env.dev-sample_ to _.env.dev_.
1. Update the environment variables in the _docker-compose.yml_ and _.env.dev_ files.
   - (M1 chip only) Remove `-slim-buster` from the Python dependency in `services/web/Dockerfile` to suppress an issue with installing psycopg2
1. Build the images and run the containers:

   ```sh
   $ docker-compose up -d --build
   ```

   Test it out at [http://localhost:5000](http://localhost:5000). The "web" folder is mounted into the container and your code changes apply automatically.
