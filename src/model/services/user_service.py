from typing import Tuple, Optional

from src.db.abstract.AUserRepository import AUserRepository
from src.db.abstract.AWordRepository import AWordRepository
from src.db.concrete.user_repo import UserRepository
from src.model.entites.users import User
import bcrypt

from src.utilits.error_messages import ErrorMessages


class UserService:
    def __init__(self, user_repo: Optional[AWordRepository] = None):
        if user_repo is None:
            self._user_repository = UserRepository()
        else:
            self._user_repository = user_repo

    def _hash_password(self, password : str) -> str:
        salt = bcrypt.gensalt() # rastgele bir salt oluşturur
        hashed_password_bytes = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password_bytes.decode("utf-8")

    def register_user(self, user_name: str, password: str, email: str) -> Tuple[Optional[User], Optional[str]]:
        """
        Yeni bir kullanıcı kayıt eder
        :param user_name:
        :param password:
        :param email:
        :return: Başarılı olursa User nesnesini döner, başarısız olur ise None ve hata mesajı döner
        """

        try:
            if not user_name or not password or not email:
                return None, ErrorMessages.fields_cannot_be_empty(["user_name", "password", "email"])
            if len(password) < 6:
                return None, ErrorMessages.password_too_short(6)

            try:
                if not User.is_valid_email(email):
                    raise ValueError(ErrorMessages.INVALID_EMAIL_FORMAT)
            except ValueError as ve:
                return None, str(ve)

            if self._user_repository.get_user_by_email(email):
                return None, ErrorMessages.EMAIL_ALREADY_EXISTS
            elif self._user_repository.get_user_by_username(user_name):
                return None, ErrorMessages.USERNAME_ALREADY_EXISTS

            hashed_password = self._hash_password(password)

            new_user = User(id=None, user_name=user_name, password_hash=hashed_password, email=email)
            new_user_id = self._user_repository.create(new_user)

            if new_user_id:
                return User(id=new_user_id, user_name=user_name, email=email, password_hash=hashed_password), None
            else:
                return None, ErrorMessages.create_operation_error("User")

        except ValueError as ve:
            return None, str(ve)
        except Exception as e:
            print(f"UserService.register_user: Genel hata: {e}")
            return None, ErrorMessages.create_operation_unexpected_error("kullanıcı")

    def delete_user(self, value) -> Tuple[bool, Optional[str]]:
        user = None

        if isinstance(value, User):
            user = self._user_repository.get_user_by_id(value.id)
            if user is None:
                return False, ErrorMessages.delete_operation_entity_could_not_be_found("kullanıcı")
        elif isinstance(value, str):
            if User.is_valid_email(value):
                user = self._user_repository.get_user_by_email(value)
                if user is None:
                    return False, ErrorMessages.delete_operation_entity_could_not_be_found("kullanıcı")
            else:
                user = self._user_repository.get_user_by_username(value)
                if user is None:
                    return False, ErrorMessages.delete_operation_entity_could_not_be_found("kullanıcı")
        elif isinstance(value, int):
            user = self._user_repository.get_user_by_id(value)
            if user is None:
                return False, ErrorMessages.delete_operation_entity_could_not_be_found("kullanıcı")

        result = self._user_repository.delete(user.id)

        if result:
            return True, None
        else:
            return False, ErrorMessages.delete_operation_error("kullanıcı")

    def update_user(self, user_id: int, user_name: str, email: str, password: str) -> Tuple[bool, Optional[str]]:

        if user_id is None or user_name is None or email is None or password is  None:
            return False, ErrorMessages.fields_cannot_be_empty(["user_id", "user_name", "email", "password"])

        if self._user_repository.get_user_by_username(user_name):
            return False, ErrorMessages.USERNAME_ALREADY_EXISTS
        elif self._user_repository.get_user_by_email(email):
            return False, ErrorMessages.EMAIL_ALREADY_EXISTS

        updated_user = self._user_repository.get_user_by_id(user_id)
        if not updated_user:
            return False, ErrorMessages.update_operation_entity_could_not_be_found("kullanıcı")

        try:
            user = User(id=user_id, user_name=user_name, password_hash=self._hash_password(password), email=email)
        except ValueError as ve:
            return False, str(ve)

        result = self._user_repository.update(user)
        return result, None

    def get_user_by_id(self, user_id: int) -> Tuple[Optional[User], Optional[str]]:

        if not user_id:
            return None, ErrorMessages.fields_cannot_be_empty(["user_id"])

        user = self._user_repository.get_user_by_id(user_id)
        if not user:
            return None, ErrorMessages.delete_operation_entity_could_not_be_found("kullanıcı")

        return user, None
