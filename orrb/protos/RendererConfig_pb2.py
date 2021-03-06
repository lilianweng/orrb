# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orrb/protos/RendererConfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='orrb/protos/RendererConfig.proto',
  package='orrb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n orrb/protos/RendererConfig.proto\x12\x04orrb\"3\n\x05\x43olor\x12\t\n\x01r\x18\x01 \x01(\x02\x12\t\n\x01g\x18\x02 \x01(\x02\x12\t\n\x01\x62\x18\x03 \x01(\x02\x12\t\n\x01\x61\x18\x04 \x01(\x02\"8\n\nQuaternion\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\t\n\x01w\x18\x04 \x01(\x02\"*\n\x07Vector3\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"\x1f\n\x07Vector2\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"q\n\x0eRendererConfig\x12\x16\n\x0emodel_xml_path\x18\x01 \x01(\t\x12\x1a\n\x12model_mapping_path\x18\x02 \x01(\t\x12+\n\ncomponents\x18\x03 \x03(\x0b\x32\x17.orrb.RendererComponent\"l\n\x11RendererComponent\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12-\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x1d.orrb.RendererComponentConfig\"\x9e\n\n\x17RendererComponentConfig\x12H\n\x0eint_properties\x18\x01 \x03(\x0b\x32\x30.orrb.RendererComponentConfig.IntPropertiesEntry\x12L\n\x10\x66loat_properties\x18\x02 \x03(\x0b\x32\x32.orrb.RendererComponentConfig.FloatPropertiesEntry\x12N\n\x11string_properties\x18\x03 \x03(\x0b\x32\x33.orrb.RendererComponentConfig.StringPropertiesEntry\x12J\n\x0f\x62ool_properties\x18\x04 \x03(\x0b\x32\x31.orrb.RendererComponentConfig.BoolPropertiesEntry\x12V\n\x15quaternion_properties\x18\x05 \x03(\x0b\x32\x37.orrb.RendererComponentConfig.QuaternionPropertiesEntry\x12P\n\x12vector3_properties\x18\x06 \x03(\x0b\x32\x34.orrb.RendererComponentConfig.Vector3PropertiesEntry\x12P\n\x12vector2_properties\x18\x07 \x03(\x0b\x32\x34.orrb.RendererComponentConfig.Vector2PropertiesEntry\x12J\n\x0f\x65num_properties\x18\x08 \x03(\x0b\x32\x31.orrb.RendererComponentConfig.EnumPropertiesEntry\x12L\n\x10\x63olor_properties\x18\t \x03(\x0b\x32\x32.orrb.RendererComponentConfig.ColorPropertiesEntry\x1a\x34\n\x12IntPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x36\n\x14\x46loatPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a\x37\n\x15StringPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x35\n\x13\x42oolPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1aM\n\x19QuaternionPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.orrb.Quaternion:\x02\x38\x01\x1aG\n\x16Vector3PropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.orrb.Vector3:\x02\x38\x01\x1aG\n\x16Vector2PropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.orrb.Vector2:\x02\x38\x01\x1a\x35\n\x13\x45numPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x43\n\x14\x43olorPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1a\n\x05value\x18\x02 \x01(\x0b\x32\x0b.orrb.Color:\x02\x38\x01\x62\x06proto3')
)




_COLOR = _descriptor.Descriptor(
  name='Color',
  full_name='orrb.Color',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='r', full_name='orrb.Color.r', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='g', full_name='orrb.Color.g', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='orrb.Color.b', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='a', full_name='orrb.Color.a', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=42,
  serialized_end=93,
)


_QUATERNION = _descriptor.Descriptor(
  name='Quaternion',
  full_name='orrb.Quaternion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='orrb.Quaternion.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='orrb.Quaternion.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='orrb.Quaternion.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w', full_name='orrb.Quaternion.w', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=95,
  serialized_end=151,
)


_VECTOR3 = _descriptor.Descriptor(
  name='Vector3',
  full_name='orrb.Vector3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='orrb.Vector3.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='orrb.Vector3.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='orrb.Vector3.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
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
  serialized_start=153,
  serialized_end=195,
)


_VECTOR2 = _descriptor.Descriptor(
  name='Vector2',
  full_name='orrb.Vector2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='orrb.Vector2.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='orrb.Vector2.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_start=197,
  serialized_end=228,
)


_RENDERERCONFIG = _descriptor.Descriptor(
  name='RendererConfig',
  full_name='orrb.RendererConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_xml_path', full_name='orrb.RendererConfig.model_xml_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_mapping_path', full_name='orrb.RendererConfig.model_mapping_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='components', full_name='orrb.RendererConfig.components', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=230,
  serialized_end=343,
)


_RENDERERCOMPONENT = _descriptor.Descriptor(
  name='RendererComponent',
  full_name='orrb.RendererComponent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='orrb.RendererComponent.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='orrb.RendererComponent.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='orrb.RendererComponent.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='orrb.RendererComponent.config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=345,
  serialized_end=453,
)


_RENDERERCOMPONENTCONFIG_INTPROPERTIESENTRY = _descriptor.Descriptor(
  name='IntPropertiesEntry',
  full_name='orrb.RendererComponentConfig.IntPropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orrb.RendererComponentConfig.IntPropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='orrb.RendererComponentConfig.IntPropertiesEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1197,
  serialized_end=1249,
)

_RENDERERCOMPONENTCONFIG_FLOATPROPERTIESENTRY = _descriptor.Descriptor(
  name='FloatPropertiesEntry',
  full_name='orrb.RendererComponentConfig.FloatPropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orrb.RendererComponentConfig.FloatPropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='orrb.RendererComponentConfig.FloatPropertiesEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1251,
  serialized_end=1305,
)

_RENDERERCOMPONENTCONFIG_STRINGPROPERTIESENTRY = _descriptor.Descriptor(
  name='StringPropertiesEntry',
  full_name='orrb.RendererComponentConfig.StringPropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orrb.RendererComponentConfig.StringPropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='orrb.RendererComponentConfig.StringPropertiesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1307,
  serialized_end=1362,
)

_RENDERERCOMPONENTCONFIG_BOOLPROPERTIESENTRY = _descriptor.Descriptor(
  name='BoolPropertiesEntry',
  full_name='orrb.RendererComponentConfig.BoolPropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orrb.RendererComponentConfig.BoolPropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='orrb.RendererComponentConfig.BoolPropertiesEntry.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1364,
  serialized_end=1417,
)

_RENDERERCOMPONENTCONFIG_QUATERNIONPROPERTIESENTRY = _descriptor.Descriptor(
  name='QuaternionPropertiesEntry',
  full_name='orrb.RendererComponentConfig.QuaternionPropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orrb.RendererComponentConfig.QuaternionPropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='orrb.RendererComponentConfig.QuaternionPropertiesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1419,
  serialized_end=1496,
)

_RENDERERCOMPONENTCONFIG_VECTOR3PROPERTIESENTRY = _descriptor.Descriptor(
  name='Vector3PropertiesEntry',
  full_name='orrb.RendererComponentConfig.Vector3PropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orrb.RendererComponentConfig.Vector3PropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='orrb.RendererComponentConfig.Vector3PropertiesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1498,
  serialized_end=1569,
)

_RENDERERCOMPONENTCONFIG_VECTOR2PROPERTIESENTRY = _descriptor.Descriptor(
  name='Vector2PropertiesEntry',
  full_name='orrb.RendererComponentConfig.Vector2PropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orrb.RendererComponentConfig.Vector2PropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='orrb.RendererComponentConfig.Vector2PropertiesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1571,
  serialized_end=1642,
)

_RENDERERCOMPONENTCONFIG_ENUMPROPERTIESENTRY = _descriptor.Descriptor(
  name='EnumPropertiesEntry',
  full_name='orrb.RendererComponentConfig.EnumPropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orrb.RendererComponentConfig.EnumPropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='orrb.RendererComponentConfig.EnumPropertiesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1644,
  serialized_end=1697,
)

_RENDERERCOMPONENTCONFIG_COLORPROPERTIESENTRY = _descriptor.Descriptor(
  name='ColorPropertiesEntry',
  full_name='orrb.RendererComponentConfig.ColorPropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orrb.RendererComponentConfig.ColorPropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='orrb.RendererComponentConfig.ColorPropertiesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1699,
  serialized_end=1766,
)

_RENDERERCOMPONENTCONFIG = _descriptor.Descriptor(
  name='RendererComponentConfig',
  full_name='orrb.RendererComponentConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int_properties', full_name='orrb.RendererComponentConfig.int_properties', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_properties', full_name='orrb.RendererComponentConfig.float_properties', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_properties', full_name='orrb.RendererComponentConfig.string_properties', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_properties', full_name='orrb.RendererComponentConfig.bool_properties', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quaternion_properties', full_name='orrb.RendererComponentConfig.quaternion_properties', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vector3_properties', full_name='orrb.RendererComponentConfig.vector3_properties', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vector2_properties', full_name='orrb.RendererComponentConfig.vector2_properties', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enum_properties', full_name='orrb.RendererComponentConfig.enum_properties', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color_properties', full_name='orrb.RendererComponentConfig.color_properties', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RENDERERCOMPONENTCONFIG_INTPROPERTIESENTRY, _RENDERERCOMPONENTCONFIG_FLOATPROPERTIESENTRY, _RENDERERCOMPONENTCONFIG_STRINGPROPERTIESENTRY, _RENDERERCOMPONENTCONFIG_BOOLPROPERTIESENTRY, _RENDERERCOMPONENTCONFIG_QUATERNIONPROPERTIESENTRY, _RENDERERCOMPONENTCONFIG_VECTOR3PROPERTIESENTRY, _RENDERERCOMPONENTCONFIG_VECTOR2PROPERTIESENTRY, _RENDERERCOMPONENTCONFIG_ENUMPROPERTIESENTRY, _RENDERERCOMPONENTCONFIG_COLORPROPERTIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=456,
  serialized_end=1766,
)

_RENDERERCONFIG.fields_by_name['components'].message_type = _RENDERERCOMPONENT
_RENDERERCOMPONENT.fields_by_name['config'].message_type = _RENDERERCOMPONENTCONFIG
_RENDERERCOMPONENTCONFIG_INTPROPERTIESENTRY.containing_type = _RENDERERCOMPONENTCONFIG
_RENDERERCOMPONENTCONFIG_FLOATPROPERTIESENTRY.containing_type = _RENDERERCOMPONENTCONFIG
_RENDERERCOMPONENTCONFIG_STRINGPROPERTIESENTRY.containing_type = _RENDERERCOMPONENTCONFIG
_RENDERERCOMPONENTCONFIG_BOOLPROPERTIESENTRY.containing_type = _RENDERERCOMPONENTCONFIG
_RENDERERCOMPONENTCONFIG_QUATERNIONPROPERTIESENTRY.fields_by_name['value'].message_type = _QUATERNION
_RENDERERCOMPONENTCONFIG_QUATERNIONPROPERTIESENTRY.containing_type = _RENDERERCOMPONENTCONFIG
_RENDERERCOMPONENTCONFIG_VECTOR3PROPERTIESENTRY.fields_by_name['value'].message_type = _VECTOR3
_RENDERERCOMPONENTCONFIG_VECTOR3PROPERTIESENTRY.containing_type = _RENDERERCOMPONENTCONFIG
_RENDERERCOMPONENTCONFIG_VECTOR2PROPERTIESENTRY.fields_by_name['value'].message_type = _VECTOR2
_RENDERERCOMPONENTCONFIG_VECTOR2PROPERTIESENTRY.containing_type = _RENDERERCOMPONENTCONFIG
_RENDERERCOMPONENTCONFIG_ENUMPROPERTIESENTRY.containing_type = _RENDERERCOMPONENTCONFIG
_RENDERERCOMPONENTCONFIG_COLORPROPERTIESENTRY.fields_by_name['value'].message_type = _COLOR
_RENDERERCOMPONENTCONFIG_COLORPROPERTIESENTRY.containing_type = _RENDERERCOMPONENTCONFIG
_RENDERERCOMPONENTCONFIG.fields_by_name['int_properties'].message_type = _RENDERERCOMPONENTCONFIG_INTPROPERTIESENTRY
_RENDERERCOMPONENTCONFIG.fields_by_name['float_properties'].message_type = _RENDERERCOMPONENTCONFIG_FLOATPROPERTIESENTRY
_RENDERERCOMPONENTCONFIG.fields_by_name['string_properties'].message_type = _RENDERERCOMPONENTCONFIG_STRINGPROPERTIESENTRY
_RENDERERCOMPONENTCONFIG.fields_by_name['bool_properties'].message_type = _RENDERERCOMPONENTCONFIG_BOOLPROPERTIESENTRY
_RENDERERCOMPONENTCONFIG.fields_by_name['quaternion_properties'].message_type = _RENDERERCOMPONENTCONFIG_QUATERNIONPROPERTIESENTRY
_RENDERERCOMPONENTCONFIG.fields_by_name['vector3_properties'].message_type = _RENDERERCOMPONENTCONFIG_VECTOR3PROPERTIESENTRY
_RENDERERCOMPONENTCONFIG.fields_by_name['vector2_properties'].message_type = _RENDERERCOMPONENTCONFIG_VECTOR2PROPERTIESENTRY
_RENDERERCOMPONENTCONFIG.fields_by_name['enum_properties'].message_type = _RENDERERCOMPONENTCONFIG_ENUMPROPERTIESENTRY
_RENDERERCOMPONENTCONFIG.fields_by_name['color_properties'].message_type = _RENDERERCOMPONENTCONFIG_COLORPROPERTIESENTRY
DESCRIPTOR.message_types_by_name['Color'] = _COLOR
DESCRIPTOR.message_types_by_name['Quaternion'] = _QUATERNION
DESCRIPTOR.message_types_by_name['Vector3'] = _VECTOR3
DESCRIPTOR.message_types_by_name['Vector2'] = _VECTOR2
DESCRIPTOR.message_types_by_name['RendererConfig'] = _RENDERERCONFIG
DESCRIPTOR.message_types_by_name['RendererComponent'] = _RENDERERCOMPONENT
DESCRIPTOR.message_types_by_name['RendererComponentConfig'] = _RENDERERCOMPONENTCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Color = _reflection.GeneratedProtocolMessageType('Color', (_message.Message,), dict(
  DESCRIPTOR = _COLOR,
  __module__ = 'orrb.protos.RendererConfig_pb2'
  # @@protoc_insertion_point(class_scope:orrb.Color)
  ))
_sym_db.RegisterMessage(Color)

Quaternion = _reflection.GeneratedProtocolMessageType('Quaternion', (_message.Message,), dict(
  DESCRIPTOR = _QUATERNION,
  __module__ = 'orrb.protos.RendererConfig_pb2'
  # @@protoc_insertion_point(class_scope:orrb.Quaternion)
  ))
_sym_db.RegisterMessage(Quaternion)

Vector3 = _reflection.GeneratedProtocolMessageType('Vector3', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR3,
  __module__ = 'orrb.protos.RendererConfig_pb2'
  # @@protoc_insertion_point(class_scope:orrb.Vector3)
  ))
_sym_db.RegisterMessage(Vector3)

Vector2 = _reflection.GeneratedProtocolMessageType('Vector2', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR2,
  __module__ = 'orrb.protos.RendererConfig_pb2'
  # @@protoc_insertion_point(class_scope:orrb.Vector2)
  ))
_sym_db.RegisterMessage(Vector2)

RendererConfig = _reflection.GeneratedProtocolMessageType('RendererConfig', (_message.Message,), dict(
  DESCRIPTOR = _RENDERERCONFIG,
  __module__ = 'orrb.protos.RendererConfig_pb2'
  # @@protoc_insertion_point(class_scope:orrb.RendererConfig)
  ))
_sym_db.RegisterMessage(RendererConfig)

RendererComponent = _reflection.GeneratedProtocolMessageType('RendererComponent', (_message.Message,), dict(
  DESCRIPTOR = _RENDERERCOMPONENT,
  __module__ = 'orrb.protos.RendererConfig_pb2'
  # @@protoc_insertion_point(class_scope:orrb.RendererComponent)
  ))
_sym_db.RegisterMessage(RendererComponent)

RendererComponentConfig = _reflection.GeneratedProtocolMessageType('RendererComponentConfig', (_message.Message,), dict(

  IntPropertiesEntry = _reflection.GeneratedProtocolMessageType('IntPropertiesEntry', (_message.Message,), dict(
    DESCRIPTOR = _RENDERERCOMPONENTCONFIG_INTPROPERTIESENTRY,
    __module__ = 'orrb.protos.RendererConfig_pb2'
    # @@protoc_insertion_point(class_scope:orrb.RendererComponentConfig.IntPropertiesEntry)
    ))
  ,

  FloatPropertiesEntry = _reflection.GeneratedProtocolMessageType('FloatPropertiesEntry', (_message.Message,), dict(
    DESCRIPTOR = _RENDERERCOMPONENTCONFIG_FLOATPROPERTIESENTRY,
    __module__ = 'orrb.protos.RendererConfig_pb2'
    # @@protoc_insertion_point(class_scope:orrb.RendererComponentConfig.FloatPropertiesEntry)
    ))
  ,

  StringPropertiesEntry = _reflection.GeneratedProtocolMessageType('StringPropertiesEntry', (_message.Message,), dict(
    DESCRIPTOR = _RENDERERCOMPONENTCONFIG_STRINGPROPERTIESENTRY,
    __module__ = 'orrb.protos.RendererConfig_pb2'
    # @@protoc_insertion_point(class_scope:orrb.RendererComponentConfig.StringPropertiesEntry)
    ))
  ,

  BoolPropertiesEntry = _reflection.GeneratedProtocolMessageType('BoolPropertiesEntry', (_message.Message,), dict(
    DESCRIPTOR = _RENDERERCOMPONENTCONFIG_BOOLPROPERTIESENTRY,
    __module__ = 'orrb.protos.RendererConfig_pb2'
    # @@protoc_insertion_point(class_scope:orrb.RendererComponentConfig.BoolPropertiesEntry)
    ))
  ,

  QuaternionPropertiesEntry = _reflection.GeneratedProtocolMessageType('QuaternionPropertiesEntry', (_message.Message,), dict(
    DESCRIPTOR = _RENDERERCOMPONENTCONFIG_QUATERNIONPROPERTIESENTRY,
    __module__ = 'orrb.protos.RendererConfig_pb2'
    # @@protoc_insertion_point(class_scope:orrb.RendererComponentConfig.QuaternionPropertiesEntry)
    ))
  ,

  Vector3PropertiesEntry = _reflection.GeneratedProtocolMessageType('Vector3PropertiesEntry', (_message.Message,), dict(
    DESCRIPTOR = _RENDERERCOMPONENTCONFIG_VECTOR3PROPERTIESENTRY,
    __module__ = 'orrb.protos.RendererConfig_pb2'
    # @@protoc_insertion_point(class_scope:orrb.RendererComponentConfig.Vector3PropertiesEntry)
    ))
  ,

  Vector2PropertiesEntry = _reflection.GeneratedProtocolMessageType('Vector2PropertiesEntry', (_message.Message,), dict(
    DESCRIPTOR = _RENDERERCOMPONENTCONFIG_VECTOR2PROPERTIESENTRY,
    __module__ = 'orrb.protos.RendererConfig_pb2'
    # @@protoc_insertion_point(class_scope:orrb.RendererComponentConfig.Vector2PropertiesEntry)
    ))
  ,

  EnumPropertiesEntry = _reflection.GeneratedProtocolMessageType('EnumPropertiesEntry', (_message.Message,), dict(
    DESCRIPTOR = _RENDERERCOMPONENTCONFIG_ENUMPROPERTIESENTRY,
    __module__ = 'orrb.protos.RendererConfig_pb2'
    # @@protoc_insertion_point(class_scope:orrb.RendererComponentConfig.EnumPropertiesEntry)
    ))
  ,

  ColorPropertiesEntry = _reflection.GeneratedProtocolMessageType('ColorPropertiesEntry', (_message.Message,), dict(
    DESCRIPTOR = _RENDERERCOMPONENTCONFIG_COLORPROPERTIESENTRY,
    __module__ = 'orrb.protos.RendererConfig_pb2'
    # @@protoc_insertion_point(class_scope:orrb.RendererComponentConfig.ColorPropertiesEntry)
    ))
  ,
  DESCRIPTOR = _RENDERERCOMPONENTCONFIG,
  __module__ = 'orrb.protos.RendererConfig_pb2'
  # @@protoc_insertion_point(class_scope:orrb.RendererComponentConfig)
  ))
_sym_db.RegisterMessage(RendererComponentConfig)
_sym_db.RegisterMessage(RendererComponentConfig.IntPropertiesEntry)
_sym_db.RegisterMessage(RendererComponentConfig.FloatPropertiesEntry)
_sym_db.RegisterMessage(RendererComponentConfig.StringPropertiesEntry)
_sym_db.RegisterMessage(RendererComponentConfig.BoolPropertiesEntry)
_sym_db.RegisterMessage(RendererComponentConfig.QuaternionPropertiesEntry)
_sym_db.RegisterMessage(RendererComponentConfig.Vector3PropertiesEntry)
_sym_db.RegisterMessage(RendererComponentConfig.Vector2PropertiesEntry)
_sym_db.RegisterMessage(RendererComponentConfig.EnumPropertiesEntry)
_sym_db.RegisterMessage(RendererComponentConfig.ColorPropertiesEntry)


_RENDERERCOMPONENTCONFIG_INTPROPERTIESENTRY._options = None
_RENDERERCOMPONENTCONFIG_FLOATPROPERTIESENTRY._options = None
_RENDERERCOMPONENTCONFIG_STRINGPROPERTIESENTRY._options = None
_RENDERERCOMPONENTCONFIG_BOOLPROPERTIESENTRY._options = None
_RENDERERCOMPONENTCONFIG_QUATERNIONPROPERTIESENTRY._options = None
_RENDERERCOMPONENTCONFIG_VECTOR3PROPERTIESENTRY._options = None
_RENDERERCOMPONENTCONFIG_VECTOR2PROPERTIESENTRY._options = None
_RENDERERCOMPONENTCONFIG_ENUMPROPERTIESENTRY._options = None
_RENDERERCOMPONENTCONFIG_COLORPROPERTIESENTRY._options = None
# @@protoc_insertion_point(module_scope)
