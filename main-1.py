"""
from kivymd.uix.textfield import (
    MDTextField,
)

from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Gray"
        return MDScreen(
            MDTextField(
                mode="filled",
                size_hint_x=0.3,
                width="240dp",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            ),
            md_bg_color=self.theme_cls.backgroundColor,
        )


Example().run()

"""
from kivymd.uix.textfield import (
    MDTextField,
)
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDButton
from kivymd.uix.screen import MDScreen
#from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
import kivymd.uix.boxlayout

class LoginApp(MDApp):
    def build(self):
        # Set the primary color palette for the app
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        
        # Create the login screen with a vertical layout
        return MDScreen(
            kivymd.uix.boxlayout(
                orientation="vertical",
                spacing="20dp",
                size_hint=(0.8, None),
                height="300dp",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                children=[
                    MDTextField(
                        hint_text="Логин",
                        mode="filled",
                        size_hint_x=1,
                    ),
                    MDTextField(
                        hint_text="Пароль",
                        mode="filled",
                        password=True,
                        size_hint_x=1,
                    ),
                ],
            ),
            md_bg_color=self.theme_cls.bg_light
        )

# Run the app
LoginApp().run()
