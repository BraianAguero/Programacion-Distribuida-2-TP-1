FROM python:3.10.7

RUN python -m pip install --upgrade pip
RUN python -m pip install grpcio
RUN python -m pip install grpcio-tools
RUN python -m pip install pytz
COPY ./recursos /app
#RUN python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/timezone.proto
COPY ./server.py /app

WORKDIR /app/
#CMD [ "python", "/app/server.py"]