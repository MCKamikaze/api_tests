# Nationalize API tests

## Introduction
The following code tests the following API endpoints for consistency on retrieving parametrs based on randomly generated names.

## Tested API endpoints

* https://api.agify.io?name=x (returns a person's age according to his name)
* https://api.genderize.io?name=x (returns a person's gender according to his name)
* https://api.nationalize.io?name=x (returns a person's nationality according to his name)

## How to run

* Note - make sure to have Docker installed on the host.

1 . To build the image, run the following from inside the project directory:

```bash
docker build -t api_tests .
```

2. To run the tests as a Docker Container, run:

```bash
docker run api_tests
```

## Configurable flags
* --n : Number of people to generate

    can be used with Docker as well, simply add the flags to the 'docker run' command, i.e:

    ```bash
    docker run api_tests --n 10
    ```