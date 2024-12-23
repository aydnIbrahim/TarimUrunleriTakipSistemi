# Pages/PageCiftlikEkle.py

class PageCiftlikEkle:

    def __init__(self, ui):
        super().__init__()
        self.ui = ui

    def show_ciftlik_ekle_page(self):
        print("Page Çiftlik Ekle göster fonksiyonu içinde.")
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageCiftlikEkle)
