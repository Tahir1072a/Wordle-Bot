class ErrorMessages:
    EMAIL_ALREADY_EXISTS = "Bu e-posta adresi zaten kayıtlı"
    USERNAME_ALREADY_EXISTS = "Bu kullanıcı adı zaten kullanılıyor"
    INVALID_EMAIL_FORMAT = "Geçersiz email formatı girdiniz"


    @staticmethod
    def create_operation_error(entity_name: str) -> str:
        return f"{entity_name} oluşturulurken bir veritabanı hatası oluştu!"
    @staticmethod
    def create_operation_unexpected_error(entity_name: str) -> str:
        return f"{entity_name} oluşturulurken beklenmedik bir hata meydana geldi"
    @staticmethod
    def fields_cannot_be_empty(fields: list[str]) -> str:
        n = len(fields)

        if n == 1:
            return f"{fields[0]} alanı dolu olmalıdır"
        elif n == 2:
            return f"{fields[0]} ve {fields[1]} alanı dolu olmalıdır"

        first_part = ", ".join(fields[:-1])
        return f"{first_part} ve {fields[-1]} alanları dolu olmalıdır"
    @staticmethod
    def password_too_short(password_length: int) -> str:
        return f"Girilen şifre {password_length}'den uzun olmalıdır"
    @staticmethod
    def delete_operation_entity_could_not_be_found(entity_name: str) -> str:
        return f"Böyle bir {entity_name} bulunamadı!"
    @staticmethod
    def delete_operation_error(entity_name: str) -> str:
        return f"{entity_name} silinirken bir veritabanı hatası oluştu"
    @staticmethod
    def update_operation_entity_could_not_be_found(entity_name: str) -> str:
        return f"Böyle bir {entity_name} veritabanına kayıtlı değildir!"