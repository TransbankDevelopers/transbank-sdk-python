SHELL := /bin/bash

all: build run

run: build
	docker-compose run --rm web

build: .built .bundled

.built: Dockerfile
	docker-compose build
	touch .built

.bundled: Pipfile
	docker-compose run web pipenv install
	touch .bundled

logs:
	docker-compose logs

clean:
	docker-compose rm
	rm .built
	rm .bundled
