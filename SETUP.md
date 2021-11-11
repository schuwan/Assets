# Prerequisites

 - PostgreSql Server version 13
 - AWS S3
    - Bucket should be named `reverse-social-media`
    - All fiiles in the bucket need to be publicly accessible
 - Docker
    - Docker Compose

# Setting up environment
## Database

In order to create the schema needed for the application, you'll first want to log into your PostgreSql instance and run the `setup.sql` file. This file also contains some dummy data, to not include this data only run up to line 163 in the file.

## Environment file

To keep our credentials secret we used an enviorment file we pass into docker-compose via the `--env-file` option. You can use the `example.env` file as a base. I'll explain all the properties you need to set.

`DB_URL`

This should be the jdbc url used to connect to your database

`DB_USERNAME`

Username needed to connect to your database

`DB_PASSWORD`

Password needed to connect to your database

`SECRET`

This should be at least 64 random bytes that are then base 64 encoded. This is used for verfying and creating JWTs

`DISCOVERY_USER`

This is a htaccess user for accessing the eureka server dashboard. I would recommend this site for generating this [https://www.web2generators.com/apache-tools/htpasswd-generator](https://www.web2generators.com/apache-tools/htpasswd-generator)

`AWS_ACCESS_KEY`

This is the access key for your S3 bucket

`AWS_SECRET_KEY`

This is the secret key for your s3 bucket

# Running the project

To run the project all you need to do is clone the repository and then run docker compose

cloning the repo:
```
git clone https://github.com/Revature-Reverse/Assets.git && cd Assets
```

and then run docker compose

```
docker-compose --env-file </path/to/envfile.env> up -d
```

After this you should be able to access the reverse website on port 80
