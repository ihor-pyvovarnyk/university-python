export ENV_BIN=env/bin
export PYTHONPATH=$(shell pwd)
export DATABASE_CONTAINER_NAME=lab3-db

db-up: db-down
	docker run --name=$(DATABASE_CONTAINER_NAME) -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres

apply-migrations:
	$(ENV_BIN)/alembic upgrade head

db-down:
	docker rm -f $(DATABASE_CONTAINER_NAME) || true

check-models:
	$(ENV_BIN)/python lab3/check_models.py
