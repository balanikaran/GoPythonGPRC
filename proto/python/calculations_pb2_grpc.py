# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import calculations_pb2 as calculations__pb2


class CalculateStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.add = channel.unary_unary(
        '/calculations.Calculate/add',
        request_serializer=calculations__pb2.NumAB.SerializeToString,
        response_deserializer=calculations__pb2.ResAB.FromString,
        )
    self.subtract = channel.unary_unary(
        '/calculations.Calculate/subtract',
        request_serializer=calculations__pb2.NumAB.SerializeToString,
        response_deserializer=calculations__pb2.ResAB.FromString,
        )
    self.multiply = channel.unary_unary(
        '/calculations.Calculate/multiply',
        request_serializer=calculations__pb2.NumAB.SerializeToString,
        response_deserializer=calculations__pb2.ResAB.FromString,
        )
    self.divide = channel.unary_unary(
        '/calculations.Calculate/divide',
        request_serializer=calculations__pb2.NumAB.SerializeToString,
        response_deserializer=calculations__pb2.ResAB.FromString,
        )


class CalculateServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def add(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def subtract(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def multiply(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def divide(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CalculateServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'add': grpc.unary_unary_rpc_method_handler(
          servicer.add,
          request_deserializer=calculations__pb2.NumAB.FromString,
          response_serializer=calculations__pb2.ResAB.SerializeToString,
      ),
      'subtract': grpc.unary_unary_rpc_method_handler(
          servicer.subtract,
          request_deserializer=calculations__pb2.NumAB.FromString,
          response_serializer=calculations__pb2.ResAB.SerializeToString,
      ),
      'multiply': grpc.unary_unary_rpc_method_handler(
          servicer.multiply,
          request_deserializer=calculations__pb2.NumAB.FromString,
          response_serializer=calculations__pb2.ResAB.SerializeToString,
      ),
      'divide': grpc.unary_unary_rpc_method_handler(
          servicer.divide,
          request_deserializer=calculations__pb2.NumAB.FromString,
          response_serializer=calculations__pb2.ResAB.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'calculations.Calculate', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
