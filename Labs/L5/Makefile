export ENV_BIN=env/bin
export PYTHONPATH=$(shell pwd)
export DATABASE_CONTAINER_NAME=lab5-db

db-up: db-down
	docker run --name=$(DATABASE_CONTAINER_NAME) -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres
	sleep 5
	$(MAKE) apply-migrations

apply-migrations:
	$(ENV_BIN)/alembic upgrade head

db-down:
	docker rm -f $(DATABASE_CONTAINER_NAME) || true

run-with-flask: export FLASK_APP=lab5/app.py
run-with-flask: export FLASK_ENV=development
run-with-flask: db-up
	flask run

run-with-gunicorn: db-up
	gunicorn -b 127.0.0.1:5000 --log-level DEBUG lab5.app:app
