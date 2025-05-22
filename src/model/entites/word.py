from typing import Optional


class Word:
    def __init__(self, id : Optional[int], word: str):
        self.id = id
        self.word = word

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value