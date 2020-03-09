# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculations.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculations.proto',
  package='calculations',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x12\x63\x61lculations.proto\x12\x0c\x63\x61lculations\"\x1d\n\x05NumAB\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\t\n\x01\x62\x18\x02 \x01(\x01\"\x14\n\x05ResAB\x12\x0b\n\x03\x61ns\x18\x01 \x01(\x01\x32\xdc\x01\n\tCalculate\x12/\n\x03\x61\x64\x64\x12\x13.calculations.NumAB\x1a\x13.calculations.ResAB\x12\x34\n\x08subtract\x12\x13.calculations.NumAB\x1a\x13.calculations.ResAB\x12\x34\n\x08multiply\x12\x13.calculations.NumAB\x1a\x13.calculations.ResAB\x12\x32\n\x06\x64ivide\x12\x13.calculations.NumAB\x1a\x13.calculations.ResABb\x06proto3'
)




_NUMAB = _descriptor.Descriptor(
  name='NumAB',
  full_name='calculations.NumAB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='calculations.NumAB.a', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='calculations.NumAB.b', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=36,
  serialized_end=65,
)


_RESAB = _descriptor.Descriptor(
  name='ResAB',
  full_name='calculations.ResAB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ans', full_name='calculations.ResAB.ans', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=67,
  serialized_end=87,
)

DESCRIPTOR.message_types_by_name['NumAB'] = _NUMAB
DESCRIPTOR.message_types_by_name['ResAB'] = _RESAB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NumAB = _reflection.GeneratedProtocolMessageType('NumAB', (_message.Message,), {
  'DESCRIPTOR' : _NUMAB,
  '__module__' : 'calculations_pb2'
  # @@protoc_insertion_point(class_scope:calculations.NumAB)
  })
_sym_db.RegisterMessage(NumAB)

ResAB = _reflection.GeneratedProtocolMessageType('ResAB', (_message.Message,), {
  'DESCRIPTOR' : _RESAB,
  '__module__' : 'calculations_pb2'
  # @@protoc_insertion_point(class_scope:calculations.ResAB)
  })
_sym_db.RegisterMessage(ResAB)



_CALCULATE = _descriptor.ServiceDescriptor(
  name='Calculate',
  full_name='calculations.Calculate',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=90,
  serialized_end=310,
  methods=[
  _descriptor.MethodDescriptor(
    name='add',
    full_name='calculations.Calculate.add',
    index=0,
    containing_service=None,
    input_type=_NUMAB,
    output_type=_RESAB,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='subtract',
    full_name='calculations.Calculate.subtract',
    index=1,
    containing_service=None,
    input_type=_NUMAB,
    output_type=_RESAB,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='multiply',
    full_name='calculations.Calculate.multiply',
    index=2,
    containing_service=None,
    input_type=_NUMAB,
    output_type=_RESAB,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='divide',
    full_name='calculations.Calculate.divide',
    index=3,
    containing_service=None,
    input_type=_NUMAB,
    output_type=_RESAB,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATE)

DESCRIPTOR.services_by_name['Calculate'] = _CALCULATE

# @@protoc_insertion_point(module_scope)
