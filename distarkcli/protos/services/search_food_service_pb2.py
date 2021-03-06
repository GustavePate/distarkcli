# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import objects.food_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='services/search_food_service.proto',
  package='',
  serialized_pb='\n\"services/search_food_service.proto\x1a\x12objects/food.proto\"/\n\x13PBSearchFoodRequest\x12\x18\n\x10request_food_str\x18\x01 \x02(\t\"t\n\x14PBSearchFoodResponse\x12\x16\n\x05\x66oods\x18\x01 \x03(\x0b\x32\x07.PBFood\x12,\n\x0f\x66unc_error_code\x18\x02 \x02(\x0e\x32\x13.PBSearchFoodErrors\x12\x16\n\x0e\x66unc_error_msg\x18\x03 \x01(\t*J\n\x12PBSearchFoodErrors\x12\x0e\n\nERROR_NONE\x10\x01\x12\x13\n\x0f\x45RROR_NO_RESULT\x10\x02\x12\x0f\n\x0b\x45RROR_OTHER\x10\x03')

_PBSEARCHFOODERRORS = descriptor.EnumDescriptor(
  name='PBSearchFoodErrors',
  full_name='PBSearchFoodErrors',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='ERROR_NONE', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERROR_NO_RESULT', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERROR_OTHER', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=225,
  serialized_end=299,
)


ERROR_NONE = 1
ERROR_NO_RESULT = 2
ERROR_OTHER = 3



_PBSEARCHFOODREQUEST = descriptor.Descriptor(
  name='PBSearchFoodRequest',
  full_name='PBSearchFoodRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='request_food_str', full_name='PBSearchFoodRequest.request_food_str', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=58,
  serialized_end=105,
)


_PBSEARCHFOODRESPONSE = descriptor.Descriptor(
  name='PBSearchFoodResponse',
  full_name='PBSearchFoodResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='foods', full_name='PBSearchFoodResponse.foods', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='func_error_code', full_name='PBSearchFoodResponse.func_error_code', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='func_error_msg', full_name='PBSearchFoodResponse.func_error_msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=107,
  serialized_end=223,
)

_PBSEARCHFOODRESPONSE.fields_by_name['foods'].message_type = objects.food_pb2._PBFOOD
_PBSEARCHFOODRESPONSE.fields_by_name['func_error_code'].enum_type = _PBSEARCHFOODERRORS
DESCRIPTOR.message_types_by_name['PBSearchFoodRequest'] = _PBSEARCHFOODREQUEST
DESCRIPTOR.message_types_by_name['PBSearchFoodResponse'] = _PBSEARCHFOODRESPONSE

class PBSearchFoodRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBSEARCHFOODREQUEST
  
  # @@protoc_insertion_point(class_scope:PBSearchFoodRequest)

class PBSearchFoodResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBSEARCHFOODRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBSearchFoodResponse)

# @@protoc_insertion_point(module_scope)
