from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QIcon, QIntValidator, QBrush, QColor
from PySide6.QtWidgets import QTableWidgetItem, QHBoxLayout, QPushButton, QLineEdit, QWidget, QMessageBox, \
    QAbstractItemView

from DB import db_queries
from Pages.PageSepet import PageSepet


def btnSepeteEkleController(urun_adi, miktar, fiyat):
    """
    Belirtilen ürünü sepete ekler.
    :param urun_adi:
    :param miktar:
    :param fiyat:
    :return:
    """

    db_queries.addToSepet((urun_adi, miktar, fiyat))


class PageUrunler:
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        self.page_sepet = PageSepet(self.ui)
        self.ui.btnSepet.clicked.connect(self.page_sepet.show_sepet_page)

    def load_urunler(self):
        """
        Veritabanından "Ürünler" Bilgilerini alır ve tableUrunler adlı tabloya ekler.
        """
        rows = db_queries.getUrunler()
        self.ui.tableUrunler.setRowCount(len(rows))

        # Satır bazlı widgetları saklamak için bir sözlük oluşturuyoruz
        self.row_widgets = {}

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

            # Satıra özgü widgetları sakla
            self.row_widgets[i] = {
                'urun_adi': row[0],
                'stok_miktari': int(row[1]),
                'fiyat': float(row[2]),
                'lineEdit': lineEditQuantity,
                'btnSepeteAt': btnSepeteAt
            }

            # Butona tıklama olayını bağla
            btnSepeteAt.clicked.connect(
                lambda checked, row_idx=i: self.handle_button_click(row_idx)
            )

            # Layout'a widget'ları ekle
            hbox_layout.addWidget(lineEditQuantity)
            hbox_layout.addWidget(btnSepeteAt)

            # Hücreye widget ekle
            cellWidget = QWidget()
            cellWidget.setLayout(hbox_layout)
            self.ui.tableUrunler.setCellWidget(i, 6, cellWidget)
            self.ui.tableUrunler.setIconSize(QSize(120, 120))

        self.ui.tableUrunler.resizeColumnsToContents()
        self.ui.tableUrunler.horizontalHeader().setStretchLastSection(True)
        self.ui.tableUrunler.setShowGrid(False)
        self.ui.tableUrunler.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableUrunler.resizeRowsToContents()

    def handle_button_click(self, row_idx):
        """
        Sepete ekle butonuna tıklandığında tetiklenir.
        """
        row_data = self.row_widgets[row_idx]
        lineEdit = row_data['lineEdit']

        miktar_text = lineEdit.text()
        if miktar_text == '' or int(miktar_text) <= 0:
            QMessageBox.warning(self.ui, "Geçersiz Miktar", "Lütfen geçerli bir miktar girin.")
            return

        miktar = int(miktar_text)
        stok_miktari = row_data['stok_miktari']

        if miktar > stok_miktari:
            QMessageBox.warning(self.ui, "Stok Yetersiz", "Yeterli stok bulunmamaktadır.")
            return

        # Sepete Ekleme Metodu
        btnSepeteEkleController(row_data['urun_adi'], miktar, (int(row_data['fiyat']) * int(miktar_text)))

        # Stok Güncelleme
        yeni_stok = stok_miktari - miktar
        self.ui.tableUrunler.setItem(row_idx, 4, QTableWidgetItem(str(yeni_stok)))
        self.row_widgets[row_idx]['stok_miktari'] = yeni_stok

    def show_urunler_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageUrunler)
        self.ui.btnUrunler.setChecked(True)
        self.ui.btnCiftlikler.setChecked(False)
        self.load_urunler()
        self.ui.btnSepet.setIcon(QIcon("Resources/cart.png"))

    def handle_btnUrunAra(self):
        founded_words = db_queries.searchUrunAd(self.ui.lineEditUrunAra.text())

3