# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import timezone_pb2
import timezone_pb2_grpc
import datetime as dt
from google.protobuf.timestamp_pb2 import Timestamp
import pytz

class TimeZone(timezone_pb2_grpc.TimeZoneServicer):
   
    
    def DateTime(self, request,context):
        current_time=dt.datetime.now(pytz.timezone(request.localizacion))
        unixEpochTime=current_time.timestamp()
        current_time_tf=current_time.strftime("%y/%m/%d, %H:%M:%S")
        return timezone_pb2.TZReply(time=current_time_tf,time_zone=request.localizacion, epoch_time=unixEpochTime)



def serve():
    print('Starting server. Listening on port 50051')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    timezone_pb2_grpc.add_TimeZoneServicer_to_server(TimeZone(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
