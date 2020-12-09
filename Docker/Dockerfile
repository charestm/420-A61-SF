FROM ubuntu:18.04

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