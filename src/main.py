from src.controller.user_controller import UserController

def main_console_test():
    """Konsol üzerinden basit bir test çalıştırması."""
    controller = UserController()  # View olmadan da controller test edilebilir

    print("--- Kayıt Denemesi 1: Başarılı Senaryo ---")
    controller.handle_registration_attempt("test_user_99", "test99@example.com", "password123", "password123")
    print("\n--- Kayıt Denemesi 2: E-posta Mevcut ---")
    controller.handle_registration_attempt("test_user_100", "test99@example.com", "password456", "password456")
    print("\n--- Kayıt Denemesi 3: Şifreler Eşleşmiyor ---")
    controller.handle_registration_attempt("test_user_101", "test101@example.com", "pass1", "pass2")
    print("\n--- Kayıt Denemesi 4: E-posta Formatı Hatalı ---")
    controller.handle_registration_attempt("test_user_102", "test102_example.com", "password123", "password123")



if __name__ == "__main__":
    # main_gui() # GUI'yi çalıştırmak için
    main_console_test()  # Konsol testini çalıştırmak için

    # DBConnector'ı kapatmayı unutma (uygulama kapanırken)
    # DBConnector().close() # Eğer her yerde aynı instance kullanılıyorsa bu işe yarar
    # Genellikle uygulama kapanışında bir cleanup rutini içinde yapılır.