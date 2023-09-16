from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


def alertas(text):
    MDDialog(title='Erro',
             text=f'{text}',
             buttons=[MDFlatButton(text='Ok',
                                   on_release=liberar_alerta())]).open()

def liberar_alerta():
    ...


