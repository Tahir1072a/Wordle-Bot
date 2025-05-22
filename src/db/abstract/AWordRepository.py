from abc import ABC, abstractmethod
from typing import Optional

from src.db.abstract.ABaseRepository import ABaseRepository
from src.model.entites.word import Word


class AWordRepository(ABaseRepository[Word], ABC):
    @abstractmethod
    def get_word_by_id(self, word_id: int) -> Optional[Word]:
        pass