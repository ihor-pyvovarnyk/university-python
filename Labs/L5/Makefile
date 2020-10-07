export PYTHONPATH=$(shell pwd)/src

db:
	docker run --name=l5-db -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres
	sleep 5
	$(MAKE) apply-migrations

apply-migrations:
	$(MAKE) -C src apply-migrations

down:
	docker kill l5-db
	docker rm l5-db

run:
	FLASK_APP=src/app.py FLASK_ENV=development flask run

gunicorn:
	gunicorn -b 127.0.0.1:5000 --log-level DEBUG app:app