# qtcreator.py

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

from Pages.PageCiftlikler import PageCiftlikler
from Pages.PageCiftlikEkle import PageCiftlikEkle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # .ui dosyasını yükle
        loader = QUiLoader()
        ui_file = "/Users/ibrahimaydin/QtProjects/QtDemo1/form.ui"
        self.ui = loader.load(ui_file)
        self.setCentralWidget(self.ui)

        self.page_ciftlikler = PageCiftlikler(self.ui)
        self.page_ciftlik_ekle = PageCiftlikEkle(self.ui)

        # Ana pencere ayarları
        self.setFixedSize(1000, 720)
        self.setWindowTitle("Tarım Ürünleri Takip Sistemi")

        # Butonların tıklama sinyallerini ilgili metodlara bağlayın
        self.ui.btnCiftlikler.clicked.connect(self.page_ciftlikler.show_ciftlikler_page)

        self.page_ciftlikler.show_ciftlikler_page()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
