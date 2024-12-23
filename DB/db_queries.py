# DB/db_queries.py

from DB.db_connection import DatabaseConnection

SERVER = 'localhost'
DATABASE = 'TarimUrunleriTakipSistemi'
USERNAME = 'SA'
PASSWORD = 'yourStrong(!)Password'


def getCiftlikler():
    """
    'Ciftlikler' tablosundan kayıtları çeker.
    """
    db = DatabaseConnection(
        server=SERVER,
        database=DATABASE,
        username=USERNAME,
        password=PASSWORD
    )
    try:
        rows = db.execute_query("""SELECT 
                                        C.ResimYolu,
                                        C.Ad AS CiftlikAdi,
                                        AT.Turu AS AraziTuru,
                                        C.Buyukluk AS Buyukluk,
                                        CONCAT(A.Mahalle, ' ', A.Sokak, ' ', A.BinaNo, ' ', A.DaireNo, ' ', 
                                        A.Sehir, '/', A.Ulke, '/' ,A.Eyalet) AS Adres,
                                        CONCAT(S.Ad, ' ', S.Soyad) AS Sahibi
                                    FROM 
                                        Ciftlikler C
                                    JOIN 
                                        AraziTurleri AT ON C.AraziTuruID = AT.AraziTuruID
                                    JOIN 
                                        Sahipler S ON C.SahipID = S.SahipID
                                    JOIN
                                        Adresler A ON C.AdresID = A.AdresID;""")
        return rows
    finally:
        db.disconnect()
