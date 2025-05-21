import pytest

from src.db.user_repo import UserRepository
from src.model.entites.users import User
from src.model.services.user_service import UserService

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
        assert created_user.password == "mocked_hash"

        mock_repo.get_user_by_username.assert_called_once_with("testuser")
        mock_repo.get_user_by_email.assert_called_once_with("testuser@gmail.com")
        mock_repo.create_user.assert_called_once()

    def test_register_user_already_exists_email(self, user_service_with_mock_repo):
        # Arrange
        service = user_service_with_mock_repo
        mock_repo = service._user_repository

        existing_user_mock = User(id=99, user_name="user1", password="password123", email="email123@gmail.com")
        mock_repo.get_user_by_email.return_value = existing_user_mock
        mock_repo.get_user_by_username.return_value = None

        # Act
        created_user, error_message = service.register_user(user_name="user1", email="email123@gmail.com",password="password123")

        assert created_user is None
        assert error_message == "Bu e-posta adresi zaten kayıtlı."

        mock_repo.create_user.assert_not_called()
        mock_repo.get_user_by_email.assert_called_once_with("email123@gmail.com")


