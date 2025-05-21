import pytest

from src.db.user_repo import UserRepository
from src.model.entites.users import User
from src.model.services.user_service import UserService
from src.utilits.error_messages import ErrorMessages


class TestUserService:

    @pytest.fixture # Fixture => testler için temel bir durum oluşturur.
    def user_service_with_mock_repo(self, mocker):
        mock_repo_instance = mocker.MagicMock(spec=UserRepository)
        service = UserService(user_repo=mock_repo_instance) #  "nesneye yama yapma" (patching an attribute on an instance)
        return service

    def test_register_user_successful(self, mocker, user_service_with_mock_repo):
        """
        User service içindeki iş mantığının düzgün çalışıp çalışmadığını kontrol eder.
        :param mocker:
        :param user_service_with_mock_repo:
        :return:
        """
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        mock_repo.get_user_by_email.return_value = None
        mock_repo.get_user_by_username.return_value = None
        mock_repo.create_user.return_value = 1

        mocker.patch.object(UserService, '_hash_password', return_value='mocked_hash')

        created_user, error_message = service.register_user(user_name="testuser", email="testuser@gmail.com",password="mocked_hash")

        assert error_message is None
        assert created_user is not None
        assert created_user.email == "testuser@gmail.com"
        assert created_user.id == 1
        assert created_user.user_name == "testuser"
        assert created_user.password_hash == "mocked_hash"

        mock_repo.get_user_by_username.assert_called_once_with("testuser")
        mock_repo.get_user_by_email.assert_called_once_with("testuser@gmail.com")
        mock_repo.create_user.assert_called_once()

    def test_register_user_already_exists_email(self, user_service_with_mock_repo):
        # Arrange
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        existing_user_mock = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")
        mock_repo.get_user_by_email.return_value = existing_user_mock
        mock_repo.get_user_by_username.return_value = None

        # Act
        created_user, error_message = service.register_user(user_name="user1", email="email123@gmail.com",password="password123")

        assert created_user is None
        assert error_message == ErrorMessages.EMAIL_ALREADY_EXISTS

        mock_repo.create_user.assert_not_called()
        mock_repo.get_user_by_email.assert_called_once_with("email123@gmail.com")

    def test_register_user_already_exists_username(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        existing_user_mock = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")
        mock_repo.get_user_by_username.return_value = existing_user_mock
        mock_repo.get_user_by_email.return_value = None

        created_user, error_message = service.register_user(user_name="user1", email="email123@gmail.com", password="password123")

        assert created_user is None
        assert error_message == ErrorMessages.USERNAME_ALREADY_EXISTS

        mock_repo.create_user.assert_not_called()
        mock_repo.get_user_by_username.assert_called_once_with(existing_user_mock.user_name)

    def test_register_user_email_format_error(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo

        wrong_email_format = "abc@com.gmail.."

        created_user, error_message = service.register_user(user_name="user1", email=wrong_email_format, password="password123")

        assert created_user is None
        assert error_message == ErrorMessages.INVALID_EMAIL_FORMAT

    def test_delete_user_by_id_successful(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        existing_user = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")
        mock_repo.get_user_by_id.return_value = existing_user

        mock_repo.delete_user.return_value = True

        result, error_message = service.delete_user(existing_user.id)

        assert result is True
        assert error_message is None

        mock_repo.delete_user.assert_called_once_with(existing_user.id)
        mock_repo.get_user_by_id.assert_called_once_with(existing_user.id)

    def test_delete_user_by_email_successful(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        existing_user = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")
        mock_repo.get_user_by_email.return_value = existing_user

        mock_repo.delete_user.return_value = True

        result, error_message = service.delete_user(existing_user.email)

        assert result is True
        assert error_message is None

        mock_repo.delete_user.assert_called_once_with(existing_user.id)
        mock_repo.get_user_by_email.assert_called_once_with(existing_user.email)

    def test_delete_user_by_username_successful(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        existing_user = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")
        mock_repo.get_user_by_username.return_value = existing_user

        mock_repo.delete_user.return_value = True

        result, error_message = service.delete_user(existing_user.user_name)

        assert result is True
        assert error_message is None

        mock_repo.delete_user.assert_called_once_with(existing_user.id)
        mock_repo.get_user_by_username.assert_called_once_with(existing_user.user_name)

    def test_delete_user_by_user_successful(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        existing_user = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")
        mock_repo.get_user_by_id.return_value = existing_user

        mock_repo.delete_user.return_value = True

        result, error_message = service.delete_user(existing_user)

        assert result is True
        assert error_message is None

        mock_repo.delete_user.assert_called_once_with(existing_user.id)
        mock_repo.get_user_by_id.assert_called_once_with(existing_user.id)

    def test_delete_user_by_id_not_found_error(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        deleted_user = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")
        mock_repo.get_user_by_id.return_value = None

        result, error_message = service.delete_user(deleted_user.id)
        assert result is False
        assert error_message == ErrorMessages.delete_operation_entity_could_not_be_found("kullanıcı")

        mock_repo.get_user_by_id.assert_called_once_with(deleted_user.id)

    def test_delete_user_by_username_not_found_error(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        deleted_user = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")
        mock_repo.get_user_by_username.return_value = None

        result, error_message = service.delete_user(deleted_user.user_name)
        assert result is False
        assert error_message == ErrorMessages.delete_operation_entity_could_not_be_found("kullanıcı")

        mock_repo.get_user_by_username.assert_called_once_with(deleted_user.user_name)

    def test_delete_user_by_email_not_found_error(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        deleted_user = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")
        mock_repo.get_user_by_email.return_value = None

        result, error_message = service.delete_user(deleted_user.email)
        assert result is False
        assert error_message == ErrorMessages.delete_operation_entity_could_not_be_found("kullanıcı")

        mock_repo.get_user_by_email.assert_called_once_with(deleted_user.email)

    def test_delete_user_by_user_not_found_error(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        deleted_user = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")
        mock_repo.get_user_by_id.return_value = None

        result, error_message = service.delete_user(deleted_user)
        assert result is False
        assert error_message == ErrorMessages.delete_operation_entity_could_not_be_found("kullanıcı")

        mock_repo.get_user_by_id.assert_called_once_with(deleted_user.id)

    def test_update_user_successful(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        updated_user = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")

        mock_repo.get_user_by_id.return_value = updated_user
        mock_repo.update_user.return_value = True
        mock_repo.get_user_by_username.return_value = None
        mock_repo.get_user_by_email.return_value = None

        result, error_message = service.update_user(user_id=updated_user.id, user_name=updated_user.user_name, email=updated_user.email, password=updated_user.password_hash)

        assert result is True
        assert error_message is None

        mock_repo.get_user_by_id.assert_called_once_with(updated_user.id)
        mock_repo.update_user.assert_called_once()

    def test_update_user_empty_fields_error(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        result, error_message = service.update_user(None, None, None, None)

        assert result is False
        assert error_message == ErrorMessages.fields_cannot_be_empty(["user_id", "user_name", "email", "password"])

        mock_repo.update_user.assert_not_called()

    def test_update_user_not_found_error(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        updated_user = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")

        mock_repo.get_user_by_id.return_value = None
        mock_repo.get_user_by_username.return_value = None
        mock_repo.get_user_by_email.return_value = None

        result, error_message = service.update_user(user_id=updated_user.id, user_name=updated_user.user_name, email=updated_user.email, password=updated_user.password_hash)

        assert result is False
        assert error_message == ErrorMessages.update_operation_entity_could_not_be_found("kullanıcı")

        mock_repo.get_user_by_id.assert_called_once_with(updated_user.id)
        mock_repo.update_user.assert_not_called()

    def test_update_user_email_format_error(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        wrong_email ="email123gmail.com"
        updated_user = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")

        mock_repo.get_user_by_id.return_value = updated_user
        mock_repo.get_user_by_username.return_value = None
        mock_repo.get_user_by_email.return_value = None

        result, error_message = service.update_user(user_id=updated_user.id, user_name=updated_user.user_name, email=wrong_email, password=updated_user.password_hash)

        assert result is False
        assert error_message == ErrorMessages.INVALID_EMAIL_FORMAT

        mock_repo.update_user.assert_not_called()
        mock_repo.get_user_by_id.assert_called_once_with(updated_user.id)

    def test_update_user_username_already_exists_error(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        updated_user = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")
        mock_repo.get_user_by_username.return_value = updated_user

        result, error_message = service.update_user(user_id=updated_user.id, user_name=updated_user.user_name, email=updated_user.email, password=updated_user.password_hash)

        assert result is False
        assert error_message == ErrorMessages.USERNAME_ALREADY_EXISTS

        mock_repo.update_user.assert_not_called()
        mock_repo.get_user_by_username.assert_called_once_with(updated_user.user_name)

    def test_update_user_email_already_exists_error(self, user_service_with_mock_repo):
        # Arrange
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        updated_user = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")
        mock_repo.get_user_by_username.return_value = None
        mock_repo.get_user_by_email.return_value = updated_user

        result, error_message = service.update_user(user_id=updated_user.id, user_name=updated_user.user_name, email=updated_user.email, password=updated_user.password_hash)

        assert result is False
        assert error_message == ErrorMessages.EMAIL_ALREADY_EXISTS

        mock_repo.update_user.assert_not_called()
        mock_repo.get_user_by_username.assert_called_once_with(updated_user.user_name)
        mock_repo.get_user_by_email.assert_called_once_with(updated_user.email)

    def test_get_user_by_id_successful(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        entity = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")
        mock_repo.get_user_by_id.return_value = entity

        result, error_message = service.get_user_by_id(99)

        assert result == entity
        assert error_message is None

        mock_repo.get_user_by_id.assert_called_once_with(entity.id)

    def test_get_user_by_id_field_error(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        entity = User(id=99, user_name="user1", password_hash="password123", email="email123@gmail.com")
        mock_repo.get_user_by_id.return_value = entity

        result, error_message = service.get_user_by_id(None)

        assert result is None
        assert error_message == ErrorMessages.fields_cannot_be_empty(["user_id"])

        mock_repo.get_user_by_id.assert_called_once_with(entity.id)

    def test_get_user_by_id_field_error(self, user_service_with_mock_repo):
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        mock_repo.get_user_by_id.return_value = None

        result, error_message = service.get_user_by_id(99)

        assert result is None
        assert error_message == ErrorMessages.delete_operation_entity_could_not_be_found("kullanıcı")

        mock_repo.get_user_by_id.assert_called_once_with(99)