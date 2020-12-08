FROM ubuntu:18.04

RUN apt update
RUN apt -y full-upgrade

RUN apt install -y python3 python3-pip
RUN pip3 install --upgrade pip

COPY ./requirements.txt /
RUN pip3 install -r requirements.txt

RUN mkdir /notebooks
RUN mkdir /root/.jupyter
COPY jupyter_notebook_config.py /root/.jupyter

EXPOSE 8888

CMD jupyter notebook /notebooks