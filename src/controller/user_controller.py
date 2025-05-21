from src.model.services.user_service import UserService


class UserController:
    def __init__(self, view_instance=None):
        self.user_service = UserService()
        self.view = view_instance

    def handle_registration_attempt(self, user_name: str, email: str, password: str, password_confirm: str):
        print(f"UserController kayıt denemesi alındı: {user_name}, {email}")

        if password != password_confirm:
            print(f"Girilen şifreler birbiri ile eşleşmiyor.")
            return

        user, error_message = self.user_service.register_user(user_name=user_name, email=email, password=password)

        if error_message:
            print(f"User Controller :{error_message}")
        elif user:
            print(f"User Controller : Kullanıcı {user.user_name} başarıyla kaydedildi.")



