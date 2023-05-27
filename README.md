## Run postgresql and pgadmin docker

    docker-compose -f docker-compose_dv.yml up --build -d
    // get docker container network ip for connect to postgresql via pgadmin http://127.0.0.1:5050/
    docker-compose -f docker-compose_dv.yml ps
    // get docker container network ip for connect to postgresql via pgadmin
    docker ps
    docker inspect {postgresql container id} | grep IPAddress
    // enter to pgadmin and create server with ip and port 5432
    192.168.80.2 or container name
    More: https://towardsdatascience.com/how-to-run-postgresql-and-pgadmin-using-docker-3a6a8ae918b5
    
## Run alembic

    For makemigration db: alembic revision --autogenerate
    For migrate changes to db: alembic upgrade head

## Run tests
    
    pytest

## Run app in localhost

    python3 main.py