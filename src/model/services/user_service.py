from typing import Tuple, Optional
from src.db.user_repo import UserRepository
from src.model.entites.users import User
import bcrypt

class UserService:
    def __init__(self):
        self._user_repository = UserRepository()

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
        :return: Başarılı olursa User nesnesini döner, başarısız olur ise None döner
        """

        try:
            if not user_name or not password or not email:
                return None, "Kulanıcı adı, e-posta ve şifre alanları dolu olmalıdır."
            if len(password) < 6:
                return None, "Şifre en az 6 karakter uzunluğunda olmalıdır."


            try:
                if not User.is_valid_email(email):
                    raise ValueError("Geçersiz e posta formatı.")
            except ValueError as ve:
                return None, str(ve)

            if self._user_repository.get_user_by_email(email):
                return None, "Bu kullanıcı zaten kayıtlı"
            elif self._user_repository.get_user_by_username(user_name):
                return None, "Bu kullanıcı zaten kayıtlı"

            hashed_password = self._hash_password(password)

            new_user = User(id=None, user_name=user_name, password=hashed_password, email=email)
            new_user_id = self._user_repository.create_user(new_user)

            if new_user_id:
                return User(id=new_user_id, user_name=user_name, email=email, password=hashed_password), None
            else:
                return None, "Kullanıcı oluşturulurken bir veritabanı hatası oluştu!"

        except ValueError as ve:
            return None, str(ve)
        except Exception as e:
            print(f"UserService.register_user genel hata: {e}")
            return None, "Beklenmedik bir hata oluştu!"




