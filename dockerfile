FROM Ubuntu

RUN apt-get update

RUN apt-get install -y python

RUN pip install streamlit
RUN pip install alive_bar
RUN pip install load_dotenv


