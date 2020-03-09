import grpc
import os
import sys

# get current directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# add proto python folder to look for imports
sys.path.append(current_dir + "/../proto/python/")

import calculations_pb2
import calculations_pb2_grpc as calculations

def client():
    serverAddress = "localhost:3080"
    channel = grpc.insecure_channel(serverAddress)

    stub = calculations.CalculateStub(channel)

    response = stub.add(calculations_pb2.NumAB(a=4.5, b=2.577))
    print("add = {}".format(response.ans))

    response = stub.subtract(calculations_pb2.NumAB(a=4.5, b=2.577))
    print("subtract = {}".format(response.ans))

    response = stub.multiply(calculations_pb2.NumAB(a=4.5, b=2.577))
    print("multiply = {}".format(response.ans))

    response = stub.divide(calculations_pb2.NumAB(a=4.5, b=2.577))
    print("divide = {}".format(response.ans))

    pass

if __name__ == "__main__":
    client()