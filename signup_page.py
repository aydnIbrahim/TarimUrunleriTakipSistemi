from tkinter import *
from tkinter import messagebox

user_id = 1
user_name_surname = ''


class SignupPage:
    def __init__(self):
        self.fg_color = '#333'
        self.fg_color_cerceve = '#ae550c'

        self.signup_page = Tk()
        self.signup_page.title("Kayıt Ol")
        self.signup_page.geometry('373x620+650+300')
        self.signup_page.resizable(False, False)

        # Ana çerçeve
        self.panel = Frame(self.signup_page, bg=self.fg_color)
        self.panel.place(x=15, y=15, width=343, height=590)

        # Hoşgeldin başlığı
        self.hosgeldin_title = Label(self.panel, text="HOŞGELDİN", fg='#fff', bg=self.fg_color,
                                     font=('Pt Mono', 40))
        self.hosgeldin_title.pack(pady=(15, 50))

        # İsim giriş çerçevesi
        self.isim_cerceve = Frame(self.panel, bg=self.fg_color)
        self.isim_cerceve.pack(pady=15, padx=20)

        Label(self.isim_cerceve, text='İsim', fg='#fff', bg=self.fg_color, font=('Pt Mono', 14)).pack(side=LEFT,
                                                                                                      padx=(5, 33))
        self.isim_entry = Entry(self.isim_cerceve, bg=self.fg_color_cerceve, fg='#fff', font=('Arial', 12))
        self.isim_entry.pack(side=LEFT, padx=5)

        # Soy isim giriş çerçevesi
        self.soy_isim_cerceve = Frame(self.panel, bg=self.fg_color)
        self.soy_isim_cerceve.pack(pady=15, padx=20)

        Label(self.soy_isim_cerceve, text='Soy isim', fg='#fff', bg=self.fg_color, font=('Pt Mono', 14)).pack(side=LEFT,
                                                                                                              padx=5)
        self.soy_isim_entry = Entry(self.soy_isim_cerceve, bg=self.fg_color_cerceve, fg='#fff', font=('Arial', 12))
        self.soy_isim_entry.pack(side=LEFT, padx=5)

        # Email giriş çerçevesi
        self.email_cerceve = Frame(self.panel, bg=self.fg_color)
        self.email_cerceve.pack(pady=15, padx=20)

        Label(self.email_cerceve, text="E-Posta", fg='#fff', bg=self.fg_color, font=('Pt Mono', 14)).pack(side=LEFT,
                                                                                                          padx=5)
        self.email_entry = Entry(self.email_cerceve, bg=self.fg_color_cerceve, fg='#fff', font=('Arial', 12))
        self.email_entry.pack(side=LEFT, padx=5)

        # Şifre giriş çerçevesi
        self.sifre_cerceve = Frame(self.panel, bg=self.fg_color)
        self.sifre_cerceve.pack(pady=15, padx=20)

        Label(self.sifre_cerceve, text='Şifre', fg='#fff', bg=self.fg_color, font=('Pt Mono', 14)).pack(side=LEFT,
                                                                                                        padx=(5, 25))
        self.sifre_entry = Entry(self.sifre_cerceve, bg=self.fg_color_cerceve, fg='#fff', font=('Arial', 12), show='*')
        self.sifre_entry.pack(side=LEFT, padx=5)

        # Şifre onayla giriş çerçevesi
        self.sifre_onayla_cerceve = Frame(self.panel, bg=self.fg_color)
        self.sifre_onayla_cerceve.pack(pady=15, padx=20)

        Label(self.sifre_onayla_cerceve, text='Şifre', fg='#fff', bg=self.fg_color, font=('Pt Mono', 14)).pack(
            side=LEFT, padx=(5, 25))
        self.sifre_entry_onayla = Entry(self.sifre_onayla_cerceve, bg=self.fg_color_cerceve, fg='#fff',
                                        font=('Arial', 12), show='*')
        self.sifre_entry_onayla.pack(side=LEFT, padx=5)

        # Kayıt ol butonu
        self.kayit_ol_buton = Button(self.panel, text='Kayıt Ol', bg='#0052cc', fg='#fff', font=('Arial', 12),
                                     command=self.kayit_ol)
        self.kayit_ol_buton.pack(pady=30)

        # Hesap varsa giriş yap butonu
        self.hesap_varsa_giris_yap_buton = Button(self.panel, text='Bir hesabın mı var? Giriş Yap!', bg=self.fg_color,
                                                  fg='#fff', font=('Arial', 10), command=self.hesap_varsa_giris_yap)
        self.hesap_varsa_giris_yap_buton.pack(pady=10)

        self.signup_page.mainloop()

    def kayit_ol(self):
        if (self.isim_entry.get() and self.soy_isim_entry.get() and self.email_entry.get() and self.sifre_entry.get()
                and self.sifre_entry_onayla.get()):
            if self.sifre_entry.get() == self.sifre_entry_onayla.get():
                result = 1
                if result:
                    self.signup_page.destroy()
                else:
                    messagebox.showerror(title='', message="Kayıt işlemi gerçekleştirilemedi.")
            else:
                messagebox.showerror(title='', message='Şifreler eşleşmiyor')
        else:
            messagebox.showerror(title='', message='Bilgiler boş olmamalıdır.')

    def hesap_varsa_giris_yap(self):
        self.signup_page.destroy()


signup_page = SignupPage()
