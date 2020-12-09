# [Choice] Ubuntu version: bionic, focal
ARG VARIANT=focal
FROM mcr.microsoft.com/vscode/devcontainers/base:${VARIANT}

# [Optional] Uncomment this section to install additional OS packages.
 #RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
 #    && apt-get -y install --no-install-recommends <your-package-list-here>
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive

# Set environment variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt update
RUN apt -y full-upgrade

RUN apt install -y python3 python3-pip
RUN pip3 install --upgrade pip

# Install Ubuntu packages
RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    ca-certificates \
    build-essential \
    curl \
    git-core \
    htop \
    pkg-config \
    unzip \
    tree \
    freetds-dev

COPY ./requirements.txt /
RUN pip3 install -r requirements.txt

RUN mkdir /notebooks
RUN mkdir /root/.jupyter
COPY jupyter_notebook_config.py /root/.jupyter

#Jupyter Notebook
#EXPOSE 8888
#CMD jupyter notebook /notebooks

#Jupyter Lab
EXPOSE 8888
CMD jupyter lab --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token='data-science'