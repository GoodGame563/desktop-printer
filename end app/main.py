from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager
 
KV = '''
ScreenManager:
    Screen1:
    Screen2:
 
<Screen1>:
    name: 'screen1'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title:"Home screen"
            elevation:20
        MDLabel:
            text: 'Screen 1'
            halign: 'center'
            font_size:30
        MDRaisedButton:
            text: 'Go to Screen 2'
            font_size:30
            on_release:
                root.manager.transition.direction ='left'
                root.manager.current = 'screen2'
 
<Screen2>:
    name: 'screen2'
    MDBoxLayout:
        orientation:'vertical'
        MDTopAppBar:
            title:"Second screen"
            elevation:20
            md_bg_color:'purple'
        MDBoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: 'Screen 2'
                font_size:30
                halign: 'center'
            MDRaisedButton:
                text: 'Go to Screen 1'
                font_size:30
                md_bg_color:'red'
                on_release:
                    root.manager.transition.direction ='right'
                    root.manager.current = 'screen1'
'''
 
class Screen1(Screen):
    pass
 
class Screen2(Screen):
    pass
 
class MyApp(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        screen_manager = ScreenManager()
        screen_manager.add_widget(Screen1(name='screen1'))
        screen_manager.add_widget(Screen2(name='screen2'))
        return screen_manager
 
if __name__ == '__main__':
    MyApp().run()