-- 1
CREATE DATABASE TarimUrunleriTakipSistemi

-- 2
USE TarimUrunleriTakipSistemi

-- 3 Adresler Tablosu
CREATE TABLE Adresler (
    AdresID INT PRIMARY KEY IDENTITY(1, 1),
    Ulke NVARCHAR(50) NOT NULL,
    Eyalet NVARCHAR(50),
    Sehir NVARCHAR(50) NOT NULL,
    Mahalle NVARCHAR(50) NOT NULL,
    Sokak NVARCHAR(50) NOT NULL,
    BinaNo INT NOT NULL,
    DaireNo INT NOT NULL
);

-- 4 Sahipler Tablosu
CREATE TABLE Sahipler (
    SahipID INT PRIMARY KEY IDENTITY(1, 1),
    AdresID INT NOT NULL,
    Ad NVARCHAR(50) NOT NULL,
    Soyad NVARCHAR(50) NOT NULL,
    Telefon NVARCHAR(30) NOT NULL,

    CONSTRAINT FK_Sahipler_Adresler FOREIGN KEY (AdresID)
        REFERENCES Adresler(AdresID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- 5 Arazi Türleri Tablosu
CREATE TABLE AraziTurleri (
    AraziTuruID INT PRIMARY KEY IDENTITY(1, 1),
    Turu NVARCHAR(50) NOT NULL,         -- Arazi türü bilgisi. (Tarla, Sera vb.) 
);

-- 6 Çiftlikler Tablosu
CREATE TABLE Ciftlikler (
    CiftlikID INT PRIMARY KEY IDENTITY(1, 1), 
    SahipID INT NOT NULL,
    AraziTuruID INT NOT NULL,
    AdresID INT NOT NULL,
    Ad NVARCHAR(100) NOT NULL,                  
    Buyukluk DECIMAL(10, 2) NOT NULL,   -- Hektar bazında arazi büyüklüğü.  
    ResimYolu NVARCHAR(100) 

    CONSTRAINT CK_AraziTurleri_Buyukluk CHECK (Buyukluk > 0),

    CONSTRAINT FK_Ciftlikler_Sahipler FOREIGN KEY (SahipID)
        REFERENCES Sahipler(SahipID)
        ON DELETE CASCADE               
        ON UPDATE CASCADE,

    CONSTRAINT FK_Ciftlikler_AraziTurler FOREIGN KEY (AraziTuruID)
        REFERENCES AraziTurleri(AraziTuruID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT FK_Ciftlikler_Adresler FOREIGN KEY (AdresID)
        REFERENCES Adresler(AdresID)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

-- 7 Kategoriler Tablosu
CREATE TABLE Kategoriler (
    KategoriID INT PRIMARY KEY IDENTITY(1, 1),
    Kategori NVARCHAR(50) NOT NULL
);

-- 8 Birimler Tablosu
CREATE TABLE Birimler (
    BirimID INT PRIMARY KEY IDENTITY(1, 1),
    Birim NVARCHAR(20) NOT NULL
);

-- 9 Ürünler Tablosu
CREATE TABLE Urunler (
    UrunID INT PRIMARY KEY IDENTITY(1, 1),
    KategoriID INT NOT NULL,
    BirimID INT NOT NULL,
    Ad NVARCHAR(100) NOT NULL,
    StokMiktari INT NOT NULL,
    BirimFiyati DECIMAL(10, 2) NOT NULL,
    ResimYolu NVVARCHAR(100),

    CONSTRAINT CK_Urunler_StokMiktari CHECK (StokMiktari > 0),

    CONSTRAINT FK_Urunler_Kategoriler FOREIGN KEY (KategoriID)
        REFERENCES Kategoriler(KategoriID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT FK_Urunler_Birimler FOREIGN KEY (BirimID)
        REFERENCES Birimler(BirimID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- 10 Hasatlar Tablosu
CREATE TABLE Hasatlar (
    HasatID INT PRIMARY KEY IDENTITY(1, 1),
    CiftlikID INT NOT NULL,  
    BirimID INT NOT NULL,               
    UrunID INT NOT NULL,                   
    Tarih DATE NOT NULL,
    Miktar INT NOT NULL,

    CONSTRAINT CK_Hasatlar_Miktar CHECK (Miktar > 0),

    CONSTRAINT FK_Hasatlar_Ciftlikler FOREIGN KEY (CiftlikID)
        REFERENCES Ciftlikler(CiftlikID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT FK_Hasatlar_Urunler FOREIGN KEY (UrunID)
        REFERENCES Urunler(UrunID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT FK_Hasatlar_Birimler FOREIGN KEY (BirimID)
        REFERENCES Birimler(BirimID)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
);

-- 11 Müşteriler Tablosu
CREATE TABLE Musteriler (
    MusteriID INT PRIMARY KEY IDENTITY(1, 1),
    Ad NVARCHAR(50) NOT NULL,
    Soyad NVARCHAR(50) NOT NULL,
    AdresID INT NOT NULL,
    Telefon NVARCHAR(30) NOT NULL,

    CONSTRAINT FK_Musteriler_MusteriAdresleri FOREIGN KEY (AdresId)
        REFERENCES Adresler(AdresID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- 12 Siparişler Tablosu
CREATE TABLE Siparisler (
    SiparisID INT PRIMARY KEY IDENTITY(1, 1),
    MusteriID INT NOT NULL,
    UrunID INT NOT NULL,
    Miktar INT NOT NULL,
    SiparisTarihi DATE NOT NULL,
    TeslimTarihi DATE,
    Fiyat DECIMAL(10, 2) NOT NULL,
    SepetBiti BIT

    CONSTRAINT FK_Siparisler_Musteriler FOREIGN KEY (MusteriID)
        REFERENCES Musteriler(MusteriID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT FK_Siparisler_Urunler FOREIGN KEY (UrunID)
        REFERENCES Urunler(UrunID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT CK_Siparisler_Miktar CHECK (Miktar > 0),
    CONSTRAINT CK_Satislar_Fiyat CHECK(Fiyat > 0),

    CONSTRAINT CK_Siparisler_SiparisTarihi CHECK (SiparisTarihi <= GETDATE()),
    CONSTRAINT CK_Siparisler_TeslimTarihi CHECK (TeslimTarihi <= GETDATE()),
    CONSTRAINT CK_Siparisler_SiparisTarihi_TeslimTarihi CHECK (SiparisTarihi <= TeslimTarihi)
);


-- 13 Satışlar Tablosu
CREATE TABLE Satislar (
    SatisID INT PRIMARY KEY IDENTITY(1, 1),
    SiparisID INT NOT NULL,

    CONSTRAINT FK_Satislar_Siparisler FOREIGN KEY (SiparisID)
        REFERENCES Siparisler(SiparisID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- 14 Şoförler Tablosu
CREATE TABLE Soforler (
    SoforID INT PRIMARY KEY IDENTITY(1, 1),
    Ad NVARCHAR(50) NOT NULL,
    Soyad NVARCHAR(50) NOT NULL,
    Adres NVARCHAR(200) NOT NULL,
    Telefon NVARCHAR(30) NOT NULL,
    EhliyetSinifi NVARCHAR(10) NOT NULL
);

-- 15 Lojistik Durumları Tablosu
CREATE TABLE LojistikDurumlari (
    DurumID INT PRIMARY KEY IDENTITY(1, 1),
    Durum NVARCHAR(50) NOT NULL
);

-- 16 Araçlar Tablosu
CREATE TABLE Araclar (
    AracID INT PRIMARY KEY IDENTITY(1, 1),
    Plaka NVARCHAR(50) NOT NULL,
    Marka NVARCHAR(50) NOT NULL,
    Model NVARCHAR(50) NOT NULL,
    Kapasite DECIMAL(10, 2) NOT NULL    -- Araç kapasitesi. Kg
);

-- 17 Lojistik Tablosu
CREATE TABLE Lojistik (
    LojistikID INT PRIMARY KEY IDENTITY(1, 1),
    SoforID INT NOT NULL,
    SatisID INT NOT NULL,
    AracID INT NOT NULL,
    DurumID INT NOT NULL,
    TahiminiTeslimTarihi DATE,
    TeslimTarihi DATE,

    CONSTRAINT FK_Lojistik_Soforler FOREIGN KEY (SoforID) 
        REFERENCES Soforler(SoforID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT FK_Lojistik_Satislar FOREIGN KEY (SatisID) 
        REFERENCES Satislar(SatisID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    
    CONSTRAINT FK_Lojistik_LojistikDurumlari FOREIGN KEY (DurumID)
        REFERENCES LojistikDurumlari(DurumID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT FK_Lojistik_Araclar FOREIGN KEY (AracID)
        REFERENCES Araclar(AracID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT CK_Lojistik_TahminiTeslimTarihi CHECK (TahiminiTeslimTarihi >= GETDATE()),
    CONSTRAINT CK_Lojistik_TeslimTarihi CHECK (TeslimTarihi <= GETDATE())

);

-- 18 Roller Tablosu
CREATE TABLE Roller (
    RolID INT PRIMARY KEY IDENTITY(1, 1),
    Rol NVARCHAR(20) NOT NULL
);

-- 19 Kullanıclar Tablosu
CREATE TABLE Kullanicilar (
    KullaniciID INT PRIMARY KEY IDENTITY(1, 1),
    RolID INT NOT NULL,
    KullaniciAdi NVARCHAR(50) NOT NULL UNIQUE,
    Sifre NVARCHAR(50) NOT NULL,
    Ad NVARCHAR(50) NOT NULL,
    SOYAD NVARCHAR(50) NOT NULL,

    CONSTRAINT FK_Kullanicilar_Roller FOREIGN KEY (RolID)
        REFERENCES Roller(RolID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);