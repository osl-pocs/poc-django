# ref: https://github.com/mamba-org/micromamba-docker/blob/main/Dockerfile

FROM condaforge/mambaforge:latest

LABEL maintainer="Ivan Ogasawara <ivan.ogasawara@gmail.com>"
LABEL org.opencontainers.image.title="PoC"
LABEL org.opencontainers.image.authors="PoC Team"
LABEL org.opencontainers.image.source="https://github.com/osl-incubator/poc-django"
LABEL org.opencontainers.image.version="latest"
LABEL org.opencontainers.image.description="PoC Django"
LABEL org.osl.poc_django.version="latest"

# it is the default, but using it here to have it explicitly
USER root

SHELL ["/bin/bash", "-c"]
# Use bash in Dockerfile RUN commands and make sure bashrc is sourced when
# executing commands with /bin/bash -c
# Needed to have the micromamba activate command configured etc.

ENV ENV_NAME=poc-django
ENV DEBIAN_FRONTEND=noninteractive
ARG UID=1000  # default value 1000
ARG GID=1000  # default value 1000

RUN apt-get update -y \
  && apt-get install -y \
    build-essential \
    zip \
    make \
    cron \
    curl \
    wget \
    sudo \
    tini \
  && rm -rf /var/lib/apt/lists/* \
    /var/cache/apt/archives \
    /tmp/* \
  && addgroup --gid ${GID} poc \
  && useradd --uid ${UID} --gid ${GID} -ms /bin/bash poc \
  && mkdir -p /opt/services \
  && chmod -R a+rwx /opt/conda /opt/services/ \
  && export ENV_NAME="$ENV_NAME" \
  && echo "poc ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/poc \
  && chmod 0440 /etc/sudoers.d/poc

USER poc

ENV PATH /opt/conda/envs/$ENV_NAME/bin:$PATH
ENV PYTHONPATH='/opt/services/poc-django:/opt/services/'

RUN mkdir -p /opt/services/poc-django
COPY --chown=poc:poc poc_django /opt/services/poc-django/poc_django
COPY --chown=poc:poc poetry.lock /opt/services/poc-django
COPY --chown=poc:poc pyproject.toml /opt/services/poc-django
COPY --chown=poc:poc conda/ /opt/services/poc-django/conda

WORKDIR /opt/services/poc-django

RUN mamba env create -n $ENV_NAME --file ./conda/dev.yaml \
  && poetry config virtualenvs.create false \
  && poetry install \
  && conda clean --all \
  && find /opt/conda/ -type f,l -name '*.a' -delete \
  && find /opt/conda/ -type f,l -name '*.pyc' -delete \
  && find /opt/conda/ -type f,l -name '*.js.map' -delete \
  && rm -rf /opt/conda/pkgs /tmp/*

RUN echo "source /opt/services/poc-django/scripts/entrypoint.sh" > ~/.bashrc

ENTRYPOINT ["tini", "--", "/opt/services/poc-django/scripts/entrypoint.sh"]
CMD ["./scripts/run.sh"]
