from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivy.properties import ObjectProperty

Window.size = (350, 580)

class EsqueciSenha(MDCard):
    def FecharRecSenha(self):
        self.parent.remove_widget(self)


class MenuLogin(MDCard):
    pass


class TelaLogin(FloatLayout):
    def AbrirRecSenha(self):
        self.add_widget(EsqueciSenha())

    def AbrirMenu(self):
        self.add_widget(MenuLogin())

class MyApp(MDApp):
    def build(self):
      #  self.theme_cls.primary_palette = "Blue"
        kv = Builder.load_file("telas.kv")
        screen = kv
        return screen


if __name__ == "__main__":
    MyApp().run()