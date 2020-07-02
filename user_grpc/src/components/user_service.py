from src.libs.mysql.mysql_client import  MySQLClient
from src.components.user_dto import UserDTO


class UserService:

    def __init__(self):
        self.mysql_client = MySQLClient()

    def insert_user(self, first_name: str, last_name: str, email: str, gender: str):
        sql = "INSERT INTO `user` (`first_name`,`last_name`,`email`,`gender`) " \
              "VALUES (%s,%s,%s,%s);"
        params = (first_name, last_name, email, gender)
        cursor = self.mysql_client.execute_query(query=sql, params=params, commit=True)
        row_id = cursor.lastrowid
        return self.get_user_by_id(row_id)

    def get_user_by_id(self, _id: int) -> UserDTO or None:
        sql = "SELECT * FROM user WHERE id = %s"
        params = (_id,)
        cursor = self.mysql_client.execute_query(query=sql, params=params)

        if cursor.rowcount > 0:
            return UserDTO().make_with_row(cursor.fetchone()).json_array
        else:
            return None
