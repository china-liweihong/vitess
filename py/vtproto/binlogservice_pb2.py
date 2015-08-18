# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: binlogservice.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import binlogdata_pb2 as binlogdata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='binlogservice.proto',
  package='binlogservice',
  syntax='proto3',
  serialized_pb=_b('\n\x13\x62inlogservice.proto\x12\rbinlogservice\x1a\x10\x62inlogdata.proto2\x99\x02\n\x0cUpdateStream\x12U\n\x0cStreamUpdate\x12\x1f.binlogdata.StreamUpdateRequest\x1a .binlogdata.StreamUpdateResponse\"\x00\x30\x01\x12[\n\x0eStreamKeyRange\x12!.binlogdata.StreamKeyRangeRequest\x1a\".binlogdata.StreamKeyRangeResponse\"\x00\x30\x01\x12U\n\x0cStreamTables\x12\x1f.binlogdata.StreamTablesRequest\x1a .binlogdata.StreamTablesResponse\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[binlogdata__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





import abc
from grpc.early_adopter import implementations
from grpc.framework.alpha import utilities
class EarlyAdopterUpdateStreamServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def StreamUpdate(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def StreamKeyRange(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def StreamTables(self, request, context):
    raise NotImplementedError()
class EarlyAdopterUpdateStreamServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterUpdateStreamStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def StreamUpdate(self, request):
    raise NotImplementedError()
  StreamUpdate.async = None
  @abc.abstractmethod
  def StreamKeyRange(self, request):
    raise NotImplementedError()
  StreamKeyRange.async = None
  @abc.abstractmethod
  def StreamTables(self, request):
    raise NotImplementedError()
  StreamTables.async = None
def early_adopter_create_UpdateStream_server(servicer, port, private_key=None, certificate_chain=None):
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  method_service_descriptions = {
    "StreamKeyRange": utilities.unary_stream_service_description(
      servicer.StreamKeyRange,
      binlogdata_pb2.StreamKeyRangeRequest.FromString,
      binlogdata_pb2.StreamKeyRangeResponse.SerializeToString,
    ),
    "StreamTables": utilities.unary_stream_service_description(
      servicer.StreamTables,
      binlogdata_pb2.StreamTablesRequest.FromString,
      binlogdata_pb2.StreamTablesResponse.SerializeToString,
    ),
    "StreamUpdate": utilities.unary_stream_service_description(
      servicer.StreamUpdate,
      binlogdata_pb2.StreamUpdateRequest.FromString,
      binlogdata_pb2.StreamUpdateResponse.SerializeToString,
    ),
  }
  return implementations.server("binlogservice.UpdateStream", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_UpdateStream_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  import binlogdata_pb2
  method_invocation_descriptions = {
    "StreamKeyRange": utilities.unary_stream_invocation_description(
      binlogdata_pb2.StreamKeyRangeRequest.SerializeToString,
      binlogdata_pb2.StreamKeyRangeResponse.FromString,
    ),
    "StreamTables": utilities.unary_stream_invocation_description(
      binlogdata_pb2.StreamTablesRequest.SerializeToString,
      binlogdata_pb2.StreamTablesResponse.FromString,
    ),
    "StreamUpdate": utilities.unary_stream_invocation_description(
      binlogdata_pb2.StreamUpdateRequest.SerializeToString,
      binlogdata_pb2.StreamUpdateResponse.FromString,
    ),
  }
  return implementations.stub("binlogservice.UpdateStream", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)
# @@protoc_insertion_point(module_scope)
