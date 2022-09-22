FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN python -m pip install --upgrade pip
RUN python -m pip install grpcio
RUN python -m pip install grpcio-tools
COPY ./app /app
RUN python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/timezone.proto

