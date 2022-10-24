FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN python -m pip install --upgrade pip
RUN python -m pip install grpcio
RUN python -m pip install grpcio-tools
RUN python -m pip install pytz
COPY ./main.py /app
COPY ./recursos /app
COPY ./client.py /app

WORKDIR /app/
