# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: timezone.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0etimezone.proto\x12\x07\x65xample\"!\n\tTZRequest\x12\x14\n\x0clocalizacion\x18\x01 \x01(\t\">\n\x07TZReply\x12\x0c\n\x04time\x18\x02 \x01(\t\x12\x11\n\ttime_zone\x18\x03 \x01(\t\x12\x12\n\nepoch_time\x18\x04 \x01(\x01\x32>\n\x08TimeZone\x12\x32\n\x08\x44\x61teTime\x12\x12.example.TZRequest\x1a\x10.example.TZReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'timezone_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TZREQUEST._serialized_start=27
  _TZREQUEST._serialized_end=60
  _TZREPLY._serialized_start=62
  _TZREPLY._serialized_end=124
  _TIMEZONE._serialized_start=126
  _TIMEZONE._serialized_end=188
# @@protoc_insertion_point(module_scope)