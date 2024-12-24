# from DB import db_queries
#
# class PageSepet:
#     def __init__(self, ui):
#         super().__init__()
#         self.ui = ui
#
#     def load_urunler(self):
#         """
#         Veritabnından 'Ürünler" bilgilerini alır ve tableSepet adlı tabloya ekler.
#         :return:
#         """
#
#         rows = db_queries.getSiparislerVeSepet()
#         self.ui.tableSepet.setRowCount(len(rows))
#
#         for i, row in enumerate(rows):
#
