FROM python

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/brasildigital-net-br/EVA.git .

WORKDIR /app/yasmin/py/

RUN pip3 install -r requirements.txt

WORKDIR /app

WORKDIR /app/yasmin/py/stramlit/

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
