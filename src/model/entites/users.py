import re
from typing import Optional

from src.utilits.error_messages import ErrorMessages


class User:
    def __init__(self, id: Optional[int], user_name: str, email: str, password_hash: str):
        self._id = id
        self.user_name = user_name
        self.email = email
        self.password_hash = password_hash

    @property
    def id(self) -> int:
        return self._id

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if self.is_valid_email(value):
            self._email = value
        else:
            raise ValueError(ErrorMessages.INVALID_EMAIL_FORMAT)

    @staticmethod
    def is_valid_email(email: str) -> bool:
        if not email:
            return False

        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(re.compile(pattern), email) is not None