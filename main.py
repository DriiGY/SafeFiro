from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.label import MDLabel

from libs.screens.homepage import HomePage

class SafefiroApp(MDApp):
    def build(self):
        Window.size = [412, 732]
        self.load_all_kv_files()
        return HomePage()

    def load_all_kv_files(self):
        Builder.load_file("./libs/screens/homepage.kv")


if __name__ == "__main__":
    SafefiroApp().run()
