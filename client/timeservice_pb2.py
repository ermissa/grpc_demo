# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: timeservice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='timeservice.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z\002pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11timeservice.proto\"\x15\n\x04Time\x12\r\n\x05value\x18\x01 \x01(\t\"!\n\nTimeUpdate\x12\x13\n\x04time\x18\x01 \x01(\x0b\x32\x05.Time\"\x0c\n\nNowRequest\"#\n\x11TimeStreamRequest\x12\x0e\n\x06length\x18\x01 \x01(\x05\x32[\n\x0bTimeService\x12\x1f\n\x03Now\x12\x0b.NowRequest\x1a\x0b.TimeUpdate\x12+\n\x06Stream\x12\x12.TimeStreamRequest\x1a\x0b.TimeUpdate0\x01\x42\x04Z\x02pbb\x06proto3'
)




_TIME = _descriptor.Descriptor(
  name='Time',
  full_name='Time',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Time.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=42,
)


_TIMEUPDATE = _descriptor.Descriptor(
  name='TimeUpdate',
  full_name='TimeUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='TimeUpdate.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=77,
)


_NOWREQUEST = _descriptor.Descriptor(
  name='NowRequest',
  full_name='NowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=91,
)


_TIMESTREAMREQUEST = _descriptor.Descriptor(
  name='TimeStreamRequest',
  full_name='TimeStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='length', full_name='TimeStreamRequest.length', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=128,
)

_TIMEUPDATE.fields_by_name['time'].message_type = _TIME
DESCRIPTOR.message_types_by_name['Time'] = _TIME
DESCRIPTOR.message_types_by_name['TimeUpdate'] = _TIMEUPDATE
DESCRIPTOR.message_types_by_name['NowRequest'] = _NOWREQUEST
DESCRIPTOR.message_types_by_name['TimeStreamRequest'] = _TIMESTREAMREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Time = _reflection.GeneratedProtocolMessageType('Time', (_message.Message,), {
  'DESCRIPTOR' : _TIME,
  '__module__' : 'timeservice_pb2'
  # @@protoc_insertion_point(class_scope:Time)
  })
_sym_db.RegisterMessage(Time)

TimeUpdate = _reflection.GeneratedProtocolMessageType('TimeUpdate', (_message.Message,), {
  'DESCRIPTOR' : _TIMEUPDATE,
  '__module__' : 'timeservice_pb2'
  # @@protoc_insertion_point(class_scope:TimeUpdate)
  })
_sym_db.RegisterMessage(TimeUpdate)

NowRequest = _reflection.GeneratedProtocolMessageType('NowRequest', (_message.Message,), {
  'DESCRIPTOR' : _NOWREQUEST,
  '__module__' : 'timeservice_pb2'
  # @@protoc_insertion_point(class_scope:NowRequest)
  })
_sym_db.RegisterMessage(NowRequest)

TimeStreamRequest = _reflection.GeneratedProtocolMessageType('TimeStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTREAMREQUEST,
  '__module__' : 'timeservice_pb2'
  # @@protoc_insertion_point(class_scope:TimeStreamRequest)
  })
_sym_db.RegisterMessage(TimeStreamRequest)


DESCRIPTOR._options = None

_TIMESERVICE = _descriptor.ServiceDescriptor(
  name='TimeService',
  full_name='TimeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=130,
  serialized_end=221,
  methods=[
  _descriptor.MethodDescriptor(
    name='Now',
    full_name='TimeService.Now',
    index=0,
    containing_service=None,
    input_type=_NOWREQUEST,
    output_type=_TIMEUPDATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Stream',
    full_name='TimeService.Stream',
    index=1,
    containing_service=None,
    input_type=_TIMESTREAMREQUEST,
    output_type=_TIMEUPDATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TIMESERVICE)

DESCRIPTOR.services_by_name['TimeService'] = _TIMESERVICE

# @@protoc_insertion_point(module_scope)