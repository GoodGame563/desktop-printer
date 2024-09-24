from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen




class EnterWindow(Screen):
    pass

class MainWindow(Screen):
    pass

class (ScreenManager):
    pass

kv = Builder.load_file('main_window.kv')

#kv = Builder.load_file('main_window.kv')
class ExampleApp(MDApp):

    def build(self):
        return kv
    


if __name__ == '__main__':
    ExampleApp().run()
