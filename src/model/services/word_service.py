from typing import Optional

from src.db.concrete.word_repo import WordRepository


class WordService:
    def __init__(self, word_repo: Optional[WordRepository] = None):
        if word_repo is None:
            self.word_repo = WordRepository()
        else:
            self.word_repo = word_repo

    def create_word(self):
        pass