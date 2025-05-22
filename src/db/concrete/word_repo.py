from typing import Optional

from src.db.abstract.AWordRepository import AWordRepository
from src.db.db_connector import DBConnector
from src.model.entites.word import Word


class WordRepository(AWordRepository):
    def __init__(self):
        self.db_connector = DBConnector()

    def create(self, word: Word) -> int:
        query = "INSERT INTO words (word) VALUES (%%s)"
        params = (word.word, )

        result = self.db_connector.execute_query(query, params)
        return result

    def get_all(self) -> list[Word]:
        query = "SELECT * FROM words"

        result = self.db_connector.execute_query(query)
        return list(result)

    def get_by_id(self, id) -> Optional[Word]:
        query = "SELECT * FROM words WHERE id = %s"
        params = (id, )

        result = self.db_connector.execute_query(query, params)
        return result

    def delete(self, id) -> bool:
        query = "DELETE * FROM words WHERE id = %s"
        params = (id, )

        result = self.db_connector.execute_query(query, params)
        return result

    def update(self, word: Word):
        query = "UPDATE words SET word = %s WHERE id = %s"
        params = (word.word, word.id)

        result = self.db_connector.execute_query(query, params)
        return result

    def get_word_by_id(self, word_id: int) -> Optional[Word]:
        query = "SELECT * FROM words WHERE id  %s"
        params = (word_id, )

        result = self.db_connector.execute_query(query, params)
        return result