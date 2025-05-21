from typing import Tuple, Optional
from src.db.user_repo import UserRepository
from src.model.entites.users import User
import bcrypt

from src.utilits.error_messages import ErrorMessages


class UserService:
    def __init__(self, user_repo: Optional[UserRepository] = None):
        if user_repo is None:
            self._user_repo = UserRepository()
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
                    raise ValueError("Geçersiz e posta formatı.")
            except ValueError as ve:
                return None, str(ve)

            if self._user_repository.get_user_by_email(email):
                return None, ErrorMessages.EMAIL_ALREADY_EXISTS
            elif self._user_repository.get_user_by_username(user_name):
                return None, ErrorMessages.USERNAME_ALREADY_EXISTS

            hashed_password = self._hash_password(password)

            new_user = User(id=None, user_name=user_name, password=hashed_password, email=email)
            new_user_id = self._user_repository.create_user(new_user)

            if new_user_id:
                return User(id=new_user_id, user_name=user_name, email=email, password=hashed_password), None
            else:
                return None, ErrorMessages.create_operation_error("User")

        except ValueError as ve:
            return None, str(ve)
        except Exception as e:
            print(f"UserService.register_user: Genel hata: {e}")
            return None, ErrorMessages.create_operation_unexpected_error("User")




