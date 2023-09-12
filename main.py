from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from random import sample


import pyodbc
import win32com.client as win32

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-9LCHIPD;"
    "Database=Teste;"
)

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

Window.size = (350, 580)


class TelaManeger(ScreenManager):
    pass


class EsqueciSenha(MDCard):
    def FecharRecSenha(self):
        self.parent.remove_widget(self)

    def enviarCodEmail(self):
        outlook = win32.Dispatch('outlook.application')
        email = outlook.CreateItem(0)

        emailfuncionario = str(self.ids.text_email.text)
        codigo = sample([1, 2, 3, 4, 5, 6, 7, 8, 9], k=4)
        email.To = "fenajole@gmail.com"
        email.Subject = "Solicitação para recuperar a senha"
        email.HTMLBody ="""
        <p>Segue seu código para recuperação da sua senha
        <p>Cód: 12345"""
        email.Send()
        print("Foi")


class TelaLogin(Screen):
    def AbrirRecSenha(self):
        self.alertaum = MDDialog(title='Erro',
                                 text=f'Informe seu email para continuar',
                                 buttons=[MDFlatButton(text='Ok',
                                                       on_release=self.liberar)])
        emailfuncionario = str(self.ids.text_email.text)
        if emailfuncionario:
            self.add_widget(EsqueciSenha())
        else:
            self.alertaum.open()

    def liberar(self, obj):
        try:
            self.alertaum.dismiss()
        except:
            self.alertadois.dismiss()


    def login(self):
        self.alertadois = MDDialog(title='Erro Login',
                              text=f'Email ou senha incorreto',
                              buttons=[MDFlatButton(text='Ok',
                                                    on_release=self.liberar)])
        emailfuncionario = str(self.ids.text_email.text)
        senhafuncionario = str(self.ids.text_senha.text)
        consultaEmail = f"""select Email from funcionarios where Email in ('{emailfuncionario}')"""
        consultaSenha = f"""select Senha from funcionarios where Senha in ('{senhafuncionario}')"""

        if cursor.execute(consultaEmail).fetchval() and cursor.execute(consultaSenha).fetchval():

            return True
        else:
            try:
                self.alertadois.open()
            except:
                print("Erro login")

class ContentNavigationDrawer(MDBoxLayout):
    pass

class TelaInicial(Screen):
    ...

class MyApp(MDApp):
    def build(self):
        kv = Builder.load_file("telas.kv")
        screen = kv
        return screen


if __name__ == "__main__":
    MyApp().run()