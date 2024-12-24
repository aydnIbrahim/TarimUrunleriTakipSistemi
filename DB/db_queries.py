# DB/db_queries.py
import pyodbc

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


def addNewCiftlik(params):
    """
    'Ciftlikler' tablosuna yeni bir çiftlik kaydı ekler.

    Parametreler:
        params (tuple): Tüm parametreler tek bir dizi veya tuple olarak gelir.
            - (ulke, eyalet, sehir, mahalle, sokak, bina_no, daire_no,
               ad, soyad, telefon, arazi_turu, ciftlik_ad, buyukluk, resim_yolu)
    """
    db = DatabaseConnection(
        server=SERVER,
        database=DATABASE,
        username=USERNAME,
        password=PASSWORD
    )

    try:
        db.connect()

        # SQL Sorgusu
        query = """
                        DECLARE @YeniAdres TABLE (AdresID INT);
                        DECLARE @YeniSahip TABLE (SahipID INT);
                        DECLARE @YeniAraziTuru TABLE (AraziTuruID INT);
                        
                        -- Adres Ekleme
                        INSERT INTO Adresler (Ulke, Eyalet, Sehir, Mahalle, Sokak, BinaNo, DaireNo)
                            OUTPUT INSERTED.AdresID INTO @YeniAdres
                            VALUES (?, ?, ?, ?, ?, ?, ?);
                        
                        -- Sahip Ekleme
                        INSERT INTO Sahipler (AdresID, Ad, Soyad, Telefon)
                            OUTPUT INSERTED.SahipID INTO @YeniSahip
                            VALUES ((SELECT AdresID FROM @YeniAdres), ?, ?, ?);
                        
                        -- Arazi Türü Kontrol ve Ekleme
                        DECLARE @YeniAraziTuruID INT;
                        IF EXISTS (SELECT 1 FROM AraziTurleri WHERE Turu = ?)
                        BEGIN
                            SELECT @YeniAraziTuruID = AraziTuruID FROM AraziTurleri WHERE Turu = ?;
                        END
                        ELSE
                        BEGIN
                            INSERT INTO AraziTurleri (Turu)
                                OUTPUT INSERTED.AraziTuruID INTO @YeniAraziTuru
                                VALUES (?);
                        
                            SET @YeniAraziTuruID = (SELECT AraziTuruID FROM @YeniAraziTuru);
                        END
                        
                        -- Çiftlik Ekleme
                        INSERT INTO Ciftlikler (SahipID, AraziTuruID, AdresID, Ad, Buyukluk, ResimYolu)
                            VALUES (
                                (SELECT SahipID FROM @YeniSahip),
                                @YeniAraziTuruID,
                                (SELECT AdresID FROM @YeniAdres),
                                ?, ?, ?
                            );
        """

        # Parametreleri sıra ile geçiriyoruz
        if len(params) != 14:
            raise ValueError("Parametre dizisi 14 değer içermelidir.")

        db.cursor.execute(query, (
            params[0], params[1], params[2], params[3], params[4], params[5], params[6],  # Adres bilgileri
            params[7], params[8], params[9],  # Sahip bilgileri
            params[10], params[10], params[10],  # Arazi Türü (Kontrol ve Ekleme için 3 kez kullanılıyor)
            params[11], params[12], params[13]  # Çiftlik bilgileri
        ))

        db.conn.commit()
        print("Yeni çiftlik başarıyla eklendi.")

    except pyodbc.Error as e:
        print(f"Hata oluştu: {e}")
        db.conn.rollback()
        raise e

    finally:
        db.disconnect()


def getUrunler():
    """
    Ürünler tablosundan kayıtları çeker.
    """
    db = DatabaseConnection(
        server=SERVER,
        database=DATABASE,
        username=USERNAME,
        password=PASSWORD
    )
    try:
        rows = db.execute_query("""SELECT
                                    U.Ad,
                                    U.StokMiktari,
                                    U.BirimFiyati,
                                    U.ResimYolu,
                                    K.Kategori,
                                    B.Birim
                                    FROM 
                                        Urunler U 
                                    JOIN
                                        Birimler AS B ON U.BirimID = B.BirimID
                                    JOIN Kategoriler AS K ON K.KategoriID = U.KategoriID;""")
        return rows
    finally:
        db.disconnect()
