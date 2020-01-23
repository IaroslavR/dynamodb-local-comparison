.PHONY: help login  build-moto build-dynalite build moto dynamodb-local dynalite start

.DEFAULT_GOAL = help

include .env
.EXPORT_ALL_VARIABLES: ;

help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

login: ## Login to the dockerhub.com
	docker login

build-moto:  ## Build moto docker image
	docker run --rm -i hadolint/hadolint < moto/Dockerfile
	docker-compose build moto

build-dynalite:  ## Build dynalite docker image
	docker run --rm -i hadolint/hadolint < dynalite/Dockerfile
	docker-compose build dynalite

build: build-dynalite build-moto

moto:
	docker stack deploy tapway --compose-file=docker-compose.moto.yml

dynamodb-local:
	docker stack deploy tapway --compose-file=docker-compose.dynamodb-local.yml

dynalite:
	docker stack deploy tapway --compose-file=docker-compose.dynalite.yml

start: dynamodb-local ## Start docker swarm stack
	docker stack deploy tapway --compose-file=docker-compose.ui.yml
