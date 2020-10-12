FROM continuumio/miniconda3

ADD requirements/environment-dev.yml /environment.yml

RUN conda config --add channels conda-forge \
  && conda update --all --yes --quiet \
  && conda install --yes conda-build \
  && conda clean -afy

RUN conda env create --name djangopoc --file /environment.yml \
  && conda clean -afy

RUN echo 'source /opt/conda/bin/activate djangopoc && exec "$@"' > activate.sh

COPY . /djangopoc
WORKDIR /djangopoc

RUN bash /activate.sh pre-commit install

ENTRYPOINT ["bash", "/activate.sh"]
