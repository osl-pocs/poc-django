MAKEFILE_DIR = $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

develop:
	pre-commit install


# docker make commands
COMPOSE_FILE := "$(MAKEFILE_DIR)/docker/docker-compose.yml"
DOCKER := PYTHON_VERSION=$(PYTHON_VERSION) docker-compose -f $(COMPOSE_FILE)
DOCKER_RUN := $(DOCKER) run --rm

docker-up:
	$(DOCKER) up -d

docker-down:
	$(DOCKER) down

docker-build:
	$(DOCKER) build --pull djangopoc

docker-pre-commit-check:
	$(DOCKER_RUN) djangopoc pre-commit run --all-files

docker-web-migrate:
	$(DOCKER) exec djangopoc bash /activate.sh python manage.py migrate

docker-test:
	# -T: Disable pseudo-tty allocation.
	$(DOCKER) exec -T djangopoc bash /activate.sh python manage.py test -v 2

docker-web-bash:
	$(DOCKER) exec --privileged djangopoc bash

docker-web-createsuperuser:
	$(DOCKER) exec --privileged djangopoc bash /activate.sh python manage.py createsuperuser

docker-web-haystack-update:
	$(DOCKER) exec --privileged djangopoc bash /activate.sh python manage.py update_index -v 2
