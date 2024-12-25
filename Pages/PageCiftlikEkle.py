# Pages/PageCiftlikEkle.py
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileDialog, QMessageBox

from DB import db_queries


class PageCiftlikEkle:

    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        self.ui.btnSelectImage.clicked.connect(self.btnSelectImageController)
        self.ui.btnApprove.clicked.connect(self.btnApproveController)
        self.ui.btnCancel.clicked.connect(self.btnCancelController)

    def show_ciftlik_ekle_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageCiftlikEkle)

        self.ui.btnApprove.setIcon(QIcon("Resources/checkmark.png"))
        self.ui.btnCancel.setIcon(QIcon("Resources/xmark.png"))

    def btnApproveController(self):
        params = [self.ui.lineEditUlke.text(), self.ui.lineEditEyaletBolge.text(), self.ui.lineEditSehir.text(),
                  self.ui.lineEditMahalle.text(), self.ui.lineEditSokak.text(), self.ui.lineEditBinaNo.text(),
                  self.ui.lineEditDaireNo.text(), self.ui.lineEditSahipAd.text(), self.ui.lineEditSahipSoyad.text(),
                  self.ui.lineEditSahipTelefon.text(), self.ui.lineEditAraziTuru.text(),
                  self.ui.lineEditCiftlikAdi.text(), self.ui.lineEditBuyukluk.text(), self.ui.btnSelectImage.text()]

        db_queries.addNewCiftlik(params)

    def btnCancelController(self):
        self.ui.lineEditUlke.setText(None)
        self.ui.lineEditEyaletBolge.setText(None)
        self.ui.lineEditSehir.setText(None)
        self.ui.lineEditMahalle.setText(None)
        self.ui.lineEditSokak.setText(None)
        self.ui.lineEditBinaNo.setText(None)
        self.ui.lineEditDaireNo.setText(None)
        self.ui.lineEditSahipAd.setText(None)
        self.ui.lineEditSahipSoyad.setText(None)
        self.ui.lineEditSahipTelefon.setText(None)
        self.ui.lineEditAraziTuru.setText(None)
        self.ui.lineEditCiftlikAdi.setText(None)
        self.ui.lineEditBuyukluk.setText(None)
        self.ui.btnSelectImage.setText("Fotoğraf Seç")

        self.ui.stackedWidget.setCurrentWidget(self.ui.pageCiftlikler)

    def btnSelectImageController(self):
        """
        Kullanıcıya bir fotoğraf seçme arayüzü sunar ve seçilen dosyanın yolunu döner.
        """
        try:
            # Kullanıcıya resim dosyaları için bir dosya seçme penceresi sun
            file_dialog = QFileDialog(self.ui.pageCiftlikEkle)
            file_dialog.setWindowTitle("Fotoğraf Seç")
            file_dialog.setNameFilter("Resim Dosyaları (*.png *.jpg *.jpeg *.bmp *.gif)")
            file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
            file_dialog.setOption(QFileDialog.Option.ReadOnly)

            if file_dialog.exec():
                selected_files = file_dialog.selectedFiles()
                if selected_files:
                    selected_file = selected_files[0]
                    self.ui.btnSelectImage.setText(selected_file)
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Bir hata oluştu: {e}")
