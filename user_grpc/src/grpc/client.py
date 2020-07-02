# this is just an example how you make grpc call, you can delete this
import grpc
import os

# import the generated classes
from src.grpc.libs.python import user_pb2
from src.grpc.libs.python import user_pb2_grpc


def grpc_client(hostname):
    ext_port = os.getenv('EXTERNAL_PORT', 8000)
    channel = grpc.insecure_channel("{0}:{1}".format(hostname, ext_port))

    user_stub = user_pb2_grpc.UserStub(channel)
    print("camme here")
    return user_stub
    #response = user_stub.getUsers(user_pb2.google_dot_protobuf_dot_empty__pb2.Empty())
    #print(response)
