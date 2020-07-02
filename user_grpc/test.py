from src.grpc.client import grpc_client

print("huh?")


#from src.components.user_service import UserService

#user_service = UserService()
#returned_id = user_service.insert_user("Pira", "Man", "pira@email", "male")

stub = grpc_client('192.168.99.100')

from src.grpc.libs.python.user_pb2_grpc import user__pb2

request = user__pb2.createUserRequest()
request.first_name = "billy2"
request.last_name = "bob2"
request.email = "bill2y@email"
request.gender = "male"

response = stub.createUser(request)
print(response)




