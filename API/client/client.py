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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging
from datetime import datetime
import grpc
import timezone_pb2
import timezone_pb2_grpc

def run(zona):
    print('Starting client. Listening on port 50051')
    print ('Zona: ',zona)
    with grpc.insecure_channel('server:50051') as channel:
        stub = timezone_pb2_grpc.TimeZoneStub(channel)
        response = stub.DateTime(timezone_pb2.TZRequest(localizacion=zona))
        #response = stub.DateTime(timezone_pb2.TZRequest(localizacion='America/Argentina/Buenos_Aires'))
        print ("Response.message: ",response.message)
    return response.message


if __name__ == '__main__':
    logging.basicConfig()
    run()
