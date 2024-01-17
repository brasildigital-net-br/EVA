FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive 

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    python3 \
    python3-pip \
    vim \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/brasildigital-net-br/EVA.git . 

WORKDIR /app/py

RUN pip3 install -r requirements.txt

WORKDIR /app

EXPOSE 8501

#COPY /Users/marcusaloise/Documents/yasmin/py/.env /app/py

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

RUN chmod +x startup.sh

#CMD ["./startup.sh", "--server.port=8501", "--server.address=0.0.0.0"]
