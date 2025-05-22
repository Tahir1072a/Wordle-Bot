from abc import ABC, abstractmethod
from typing import Optional

from src.db.abstract.ABaseRepository import ABaseRepository
from src.model.entites.users import User


class AUserRepository(ABaseRepository[User], ABC):
    @abstractmethod
    def get_user_by_username(self, username: str) -> Optional[User]:
        pass
    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        pass
    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        pass