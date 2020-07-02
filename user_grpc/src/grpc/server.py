import grpc
from concurrent import futures
import os
import json
# import the generated classes
from src.grpc.libs.python import user_pb2
from src.grpc.libs.python import user_pb2_grpc


# import the business logic
from src.components.user_service import UserService as UserServiceModel


# create a class to define the server functions
# derived from hello_pb2_grpc.HelloWorldServicer


class UserService(user_pb2_grpc.UserServicer):

    def createUser(self, request, context):
        first_name = request.first_name
        last_name = request.last_name
        email = request.email
        gender = request.gender

        user_service = UserServiceModel()
        response = user_pb2.createUserResponse()
        response.result = json.dumps(user_service.insert_user(first_name, last_name, email, gender))
        return response

    def getUsers(self, request, context):
        users = [
            {"first_name": "Pira", "last_name": "Man", "email": "pira@gmail.com", "gender": "female"},
            {"first_name": "Pira1", "last_name": "Man", "email": "pira@gmail.com", "gender": "female"},
            {"first_name": "Pira2", "last_name": "Man", "email": "pira@gmail.com", "gender": "female"},
        ]

        response = user_pb2.UsersResponse()
        for user in users:
            user_response = user_pb2.UserResponse()
            user_response.first_name = user["first_name"]
            user_response.last_name = user["last_name"]
            user_response.email = user["email"]
            user_response.gender = user["gender"]

            response.users.append(user_response)
        return response


def serve():
    max_workers = os.getenv('MAX_WORKERS', 10)
    app_port = os.getenv('APP_PORT', 8000)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers))

    user_pb2_grpc.add_UserServicer_to_server(UserService(), server)

    print("Starting server. Listening on port {0}.".format(app_port))
    server.add_insecure_port("[::]:{0}".format(app_port))
    server.start()
    server.wait_for_termination()
