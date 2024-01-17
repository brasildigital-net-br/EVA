#!/bin/bash

cd py/streamlit/ &&  streamlit run streamlit.py &

cd py/eduarda/

# Loop infinito
while true; do

    ./main.sh
    sleep 3600 # 1hora humilde
done
