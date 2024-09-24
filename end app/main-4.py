from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class my_layout(FloatLayout):
    pass

class myapp(MDApp):

    def build(self):
        return Builder.load_file('tyt.kv')
    
if __name__ == '__main__':
    myapp().run()