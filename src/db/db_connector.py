import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

class DBConnector:

    _instance = None # statik olarak tanımlıdır.

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBConnector, cls).__new__(cls)

            cls._instance.connection = None
        return cls._instance

    def connect(self):
        """Veritabanına bağlantı oluşturuluyor"""
        try:
            load_dotenv()
            self.connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )

            if self.connection.is_connected:
                return True
        except Error as e:
            print(f"Veritabanına bağlanırken bir hata oluştu: {e}")
            return False

    def get_connection(self):
        """Mevcut bağlantıyı döndürür, yoksa yeni bağlantı oluşturur."""
        if self.connection is None or self.connection.is_connected():
            self.connect()
        return self.connection

    def close(self):
        """Veritabanı bağlantısını kapatır."""
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            self.connection = None
            print("Veri tabanı bağlantısı kesildi!")

    def execute_query(self, query, params=None):
        """
        Bir SQL sorgusu çalıştırır ve sonucu döndürür.

        Args:
            query: Çalıştırılacak SQL sorgusu
            params: Sorgu parametreleri (opsiyonel)

        Returns:
            Sorgu sonucu veya None (hata durumunda)
        """
        try:
            connection = self.get_connection()
            cursor = connection.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if query.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()
                return result
            else:
                connection.commit()
                return cursor.lastrowid if cursor.lastrowid else True
        except Error as e:
            print(f"Sorgu çalıştırılırken bir hata meydana geldi")
            if connection.is_connected():
                connection.rollback()
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()