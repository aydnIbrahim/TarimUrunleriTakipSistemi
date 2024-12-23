# Pages/PageCiftlikler.py

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap

from PySide6.QtWidgets import QTableWidgetItem, QAbstractItemView, QHeaderView

from DB import db_queries
from Pages.PageCiftlikEkle import PageCiftlikEkle


class PageCiftlikler:

    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        self.page_ciftlik_ekle = PageCiftlikEkle(self.ui)
        self.ui.btnAddCiftlik.clicked.connect(self.page_ciftlik_ekle.show_ciftlik_ekle_page)

    def load_ciftlikler(self):
        """
        Veritabanından 'Çiftlikler' bilgilerini alır ve tableCiftlikler adlı tabloya ekler.
        """
        rows = db_queries.getCiftlikler()
        # Gelen kayıt sayısı kadar tablo satırını ayarla
        self.ui.tableCiftlikler.setRowCount(len(rows))

        for i, row in enumerate(rows):
            resim_yolu = row[0]
            pixmap = QPixmap(resim_yolu)
            icon = QIcon(pixmap)
            image_item = QTableWidgetItem()
            image_item.setIcon(icon)
            # row içindeki sütun sırası, veritabanı sorgusundaki SELECT sıralamasına göre değişir.
            ciftlik_adi_item = QTableWidgetItem(str(row[1]))
            arazi_turu_item = QTableWidgetItem(str(row[2]))
            buyukluk_item = QTableWidgetItem(str(row[3]))
            adres_item = QTableWidgetItem(str(row[4]))
            sahibi_item = QTableWidgetItem(str(row[5]))

            # Dikkat: setItem(row, column, item) column indeksleri .ui dosyasında
            # nasıl tasarladığınıza göre ayarlanmalıdır.
            self.ui.tableCiftlikler.setItem(i, 0, image_item)
            self.ui.tableCiftlikler.setItem(i, 1, ciftlik_adi_item)
            self.ui.tableCiftlikler.setItem(i, 2, arazi_turu_item)
            self.ui.tableCiftlikler.setItem(i, 3, buyukluk_item)
            self.ui.tableCiftlikler.setItem(i, 4, adres_item)
            self.ui.tableCiftlikler.setItem(i, 5, sahibi_item)

            self.ui.tableCiftlikler.setIconSize(QSize(240, 180))

        # 1) Sütunları içeriğe göre boyutlandır
        self.ui.tableCiftlikler.resizeColumnsToContents()

        # 2) Hücreleri düzenlemeye kapat
        self.ui.tableCiftlikler.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 3) Kullanıcının sütun genişliklerini değiştirmesini engelle
        self.ui.tableCiftlikler.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        # 4) Kullanıcının satır yüksekliğini değiştirmesini engelle
        self.ui.tableCiftlikler.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        # 5) Hücreleri ayıran çizgileri kapat
        self.ui.tableCiftlikler.setShowGrid(False)
        self.ui.tableCiftlikler.resizeRowsToContents()

    def show_ciftlikler_page(self):
        # pageCiftlikler'i göster
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageCiftlikler)

        # ciftliklerButton'ı "checked" yap
        self.ui.btnCiftlikler.setChecked(True)

        # Eğer ürünler butonu varsa, onu uncheck yapabilirsiniz
        self.ui.btnUrunler.setChecked(False)

        self.ui.btnAddCiftlik.setIcon(QIcon("Resources/plus.png"))
        self.load_ciftlikler()
