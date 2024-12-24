from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QIcon, QIntValidator
from PySide6.QtWidgets import QTableWidgetItem, QHBoxLayout, QPushButton, QLineEdit, QWidget, QAbstractItemView, \
    QHeaderView, QTableWidget

from DB import db_queries


class PageUrunler:
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        # self.ui.btnSepet.clicked.connect()

    def load_urunler(self):
        """
        Veritabanından "Ürünler" Bilgilerini alır ve tableUrunler adlı tabloya ekler.
        """
        rows = db_queries.getUrunler()
        self.ui.tableUrunler.setRowCount(len(rows))

        for i, row in enumerate(rows):
            # Ürün resmini ekle
            resim_yolu = row[3]
            pixmap = QPixmap(resim_yolu)
            icon = QIcon(pixmap)
            image_item = QTableWidgetItem()
            image_item.setIcon(icon)

            # Diğer ürün bilgilerini ekle
            urun_adi_item = QTableWidgetItem(str(row[0]))
            urun_stok_miktari_item = QTableWidgetItem(str(row[1]))
            urun_birim_fiyati_item = QTableWidgetItem(str(row[2]))
            urun_kategori_item = QTableWidgetItem(str(row[4]))
            urun_birim_item = QTableWidgetItem(str(row[5]))

            self.ui.tableUrunler.setItem(i, 0, image_item)
            self.ui.tableUrunler.setItem(i, 1, urun_adi_item)
            self.ui.tableUrunler.setItem(i, 2, urun_kategori_item)
            self.ui.tableUrunler.setItem(i, 3, urun_birim_fiyati_item)
            self.ui.tableUrunler.setItem(i, 4, urun_stok_miktari_item)
            self.ui.tableUrunler.setItem(i, 5, urun_birim_item)

            # HBoxLayout ve Widget oluştur
            hbox_layout = QHBoxLayout()
            hbox_layout.setContentsMargins(10, 0, 10, 0)
            hbox_layout.setSpacing(10)

            # Buton oluştur ve stil ekle
            btnSepeteAt = QPushButton("Ekle")
            btnSepeteAt.setCheckable(True)
            btnSepeteAt.setMaximumSize(QSize(150, 25))
            btnSepeteAt.setStyleSheet("""
                QPushButton {
                    background-color: #0433FF;
                    color: white;
                    border-radius: 5px;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #0417C9; 
                    border: 1px solid white;
                }
            """)

            # QLineEdit oluştur ve stil ekle
            lineEditQuantity = QLineEdit()
            lineEditQuantity.setMaximumSize(QSize(50, 25))
            lineEditQuantity.setStyleSheet("""
                QLineEdit {
                    background-color: #FFFFFF;
                    color: black;
                    border: 1px solid black; 
                    border-radius: 5px;
                }
            """)
            int_validator = QIntValidator(0, 1000)
            lineEditQuantity.setValidator(int_validator)

            # Layout'a widget'ları ekle
            hbox_layout.addWidget(lineEditQuantity)
            hbox_layout.addWidget(btnSepeteAt)

            # Hücreye widget ekle
            cellWidget = QWidget()
            cellWidget.setLayout(hbox_layout)
            self.ui.tableUrunler.setCellWidget(i, 6, cellWidget)
            self.ui.tableUrunler.setIconSize(QSize(120, 120))

        self.ui.tableUrunler.resizeColumnsToContents()
        self.ui.tableUrunler.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.tableUrunler.horizontalHeader().setStretchLastSection(True)
        self.ui.tableUrunler.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.tableUrunler.setShowGrid(False)
        self.ui.tableUrunler.resizeRowsToContents()

    def show_urunler_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageUrunler)
        self.ui.btnUrunler.setChecked(True)
        self.ui.btnCiftlikler.setChecked(False)
        self.load_urunler()
        self.ui.btnSepet.setIcon(QIcon("Resources/cart.png"))
