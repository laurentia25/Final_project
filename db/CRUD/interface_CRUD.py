from abc import ABC, abstractmethod
import sqlite3

from db.db_connection import get_db_connection


class CrudABC(ABC):
    def __init__(self):
        self.connection = get_db_connection()

    @abstractmethod
    def create(self, *args, **kwargs):
        pass

    @abstractmethod
    def read(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete(self, *args, **kwargs):
        pass