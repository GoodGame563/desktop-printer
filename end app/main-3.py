from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class FourthScreen(Screen):
    pass


class MyScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        Clock.schedule_once(self.screen_switch_one, 2)

    def screen_switch_one(self, dt):
        self.current = '_first_screen_'


class SwitchingScreenApp(App):

    def build(self):
        return MyScreenManager()


if __name__ == "__main__":
    SwitchingScreenApp().run()