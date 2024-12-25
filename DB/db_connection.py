# DB/db_connection.py

import pyodbc


class DatabaseConnection:
    def __init__(self, server, database, username, password, driver='ODBC Driver 17 for SQL Server'):
        """
        DatabaseConnection sınıfı, SQL Server veritabanına bağlanmak ve sorguları çalıştırmak için tasarlanmıştır.

        Parametreler:
            server   : Sunucu adı veya IP adresi (ör: 'localhost', 'localhost\\SQLEXPRESS', '192.168.1.10' vb.)
            database : Veritabanı adı
            username : Veritabanı kullanıcı adı
            password : Veritabanı şifresi
            driver   : ODBC sürücüsü (Varsayılan: 'ODBC Driver 17 for SQL Server')
        """
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.driver = driver
        self.conn = None
        self.cursor = None

    def connect(self):
        """ Sunucuya bağlanma işlemini gerçekleştirir. """
        if self.conn is None:
            try:
                self.conn = pyodbc.connect(
                    f"DRIVER={{{self.driver}}};"
                    f"SERVER={self.server};"
                    f"DATABASE={self.database};"
                    f"UID={self.username};"
                    f"PWD={self.password}"
                )
                self.cursor = self.conn.cursor()
            except pyodbc.Error as e:
                print(f"Bağlantı hatası oluştu: {e}")
                raise e

    def disconnect(self):
        """ Açık olan bağlantıyı kapatır. """
        try:
            if self.cursor is not None:
                self.cursor.close()
                self.cursor = None

            if self.conn is not None:
                self.conn.close()
                self.conn = None
        except pyodbc.Error as e:
            print(f"Bağlantı kapatma hatası oluştu: {e}")
            raise e

    def execute_query(self, query, params=None):
        """
        Parametre olarak alınan SQL sorgusunu çalıştırır ve sonucu döndürür.

        Parametreler:
            query: Çalıştırmak istenen SQL sorgusu (ör: "SELECT TOP 10 * FROM Adresler")
            params: Sorguya geçirilecek parametrelerin tuple veya liste formatında olması gerekir.

        Return:
            Sorgu sonucunu liste olarak döndürür.
        """
        try:
            # Bağlantı yoksa önce bağlantı kur
            if self.conn is None or self.cursor is None:
                self.connect()

            # Parametreli sorgu çalıştır
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            return self.cursor.fetchall()

        except pyodbc.Error as e:
            print(f"Sorgu çalıştırma hatası oluştu: {e}")
            self.conn.rollback()
            raise e
