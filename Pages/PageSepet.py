from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QTableWidgetItem, QAbstractItemView

from DB import db_queries


class PageSepet:
    def __init__(self, ui):
        super().__init__()
        self.toplamTutar = 0.0
        self.ui = ui

        self.ui.btnSatinAl.clicked.connect(self.handle_btnSatinAl)
        self.ui.btnGeriUrunler.clicked.connect(self.handle_btnGeriUrunler)

    def load_sepet(self):
        """
        Veritabnından 'Ürünler" bilgilerini alır ve tableSepet adlı tabloya ekler.
        :return:
        """

        rows = db_queries.getSiparislerVeSepet(0)
        self.ui.tableSepet.setRowCount(len(rows))

        for i, row in enumerate(rows):
            resim_yolu = row[0]
            pixmap = QPixmap(resim_yolu)
            icon = QIcon(pixmap)
            image_item = QTableWidgetItem()
            image_item.setIcon(icon)

            urun_adi_item = QTableWidgetItem(str(row[1]))
            urun_miktar_item = QTableWidgetItem(str(row[2]))
            urun_fiyat_item = QTableWidgetItem(str(row[3]))
            urun_kategori_item = QTableWidgetItem(str(row[4]))
            urun_birim_item = QTableWidgetItem(str(row[5]))

            self.ui.tableSepet.setItem(i, 0, image_item)
            self.ui.tableSepet.setItem(i, 1, urun_adi_item)
            self.ui.tableSepet.setItem(i, 2, urun_kategori_item)
            self.ui.tableSepet.setItem(i, 3, urun_miktar_item)
            self.ui.tableSepet.setItem(i, 4, urun_birim_item)
            self.ui.tableSepet.setItem(i, 5, urun_fiyat_item)

            try:
                fiyat = float(row[3])
                self.toplamTutar += fiyat
                self.ui.labelToplamTutar.setText(str(self.toplamTutar))
            except ValueError:
                print(f"Hatalı değer: Miktar={row[2]}, Fiyat={row[3]}")

        self.ui.tableSepet.setIconSize(QSize(120, 120))
        self.ui.tableSepet.resizeColumnsToContents()
        self.ui.tableSepet.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableSepet.horizontalHeader().setStretchLastSection(True)
        self.ui.tableSepet.setShowGrid(False)
        self.ui.tableSepet.resizeRowsToContents()

    def show_sepet_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageSepet)
        self.ui.btnSatinAl.setIcon(QIcon("Resources/buy.png"))
        self.ui.btnGeriUrunler.setIcon(QIcon("Resources/arrow.uturn.backward.png"))
        self.load_sepet()

    def handle_btnGeriUrunler(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageUrunler)

    def handle_btnSatinAl(self):
        """
        Sepetteki ürünlerin isimlerini alır ve db_queries.updateToSiparis metoduna gönderir.
        """
        urun_isimleri = []
        row_count = self.ui.tableSepet.rowCount()

        for i in range(row_count):
            item = self.ui.tableSepet.item(i, 1)  # Ürün adı 1. sütunda
            if item is not None:
                urun_isimleri.append(item.text())

        print(urun_isimleri)
        db_queries.updateToSiparis(urun_isimleri)
        self.ui.labelToplamTutar.setText(0)
        self.load_sepet()

