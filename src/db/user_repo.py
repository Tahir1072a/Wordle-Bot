from typing import Optional
from src.db.db_connector import DBConnector
from src.model.entites.users import User


class UserRepository:
    def __init__(self):
        self._db_connector = DBConnector()

    def create_user(self, user: User) -> int:
        query = "INSERT INTO users (user_name, email, password_hash) VALUES (%s, %s, %s)"
        params = (user.user_name, user.email, user.password)

        result = self._db_connector.execute_query(query, params)
        return result

    def get_user_by_username(self, user_name : str) -> Optional[User]:
        query = "SELECT * FROM users WHERE user_name = %s"
        params = (user_name,)

        result = self._db_connector.execute_query(query, params)
        return result

    def get_user_by_email(self, email: str) -> Optional[User]:
        query = "SELECT * FROM users WHERE email = %s"
        params = (email, )

        result = self._db_connector.execute_query(query, params)
        return result