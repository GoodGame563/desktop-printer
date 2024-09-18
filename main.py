from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


class AuthScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 50, 50, 50]
        self.spacing = 20

        Window.clearcolor = (1, 1, 1, 1)

        logo_layout = AnchorLayout(anchor_x='left', anchor_y='top')
        logo = Image(source='logo.png', size_hint=(0.3, 0.3)) 
        logo_layout.add_widget(logo)

        self.add_widget(logo_layout)

        # Заголовок "Авторизация"
        title_layout = AnchorLayout(anchor_x='center', anchor_y='top')
        title = Label(text="Авторизация", font_size=32, color=(0, 0, 0, 1))  # черный текст
        title_layout.add_widget(title)

        # Добавление заголовка
        self.add_widget(title_layout)

        # Вложенный BoxLayout для полей ввода и кнопки
        input_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None))
        input_layout.size = (400, 150)  # Размер области для полей ввода и кнопки

        # Поля для ввода с фиксированным размером
        self.username_input = TextInput(hint_text="Имя пользователя", size_hint=(None, None), size=(400, 40))
        self.password_input = TextInput(hint_text="Пароль", password=True, size_hint=(None, None), size=(400, 40))

        # Добавление полей ввода
        input_layout.add_widget(self.username_input)
        input_layout.add_widget(self.password_input)

        # Кнопка с фиксированным размером и синим цветом
        self.auth_button = Button(text="Войти", size_hint=(None, None), size=(400, 40),
                                  background_normal='', background_color=(0, 0, 1, 1))  # Синяя кнопка

        # Добавление кнопки
        input_layout.add_widget(self.auth_button)

        # Центрирование полей и кнопки под заголовком
        input_center = AnchorLayout(anchor_x='center', anchor_y='top')
        input_center.add_widget(input_layout)

        # Добавление всей структуры на экран
        self.add_widget(input_center)


class AuthApp(App):
    def build(self):
        return AuthScreen()


if __name__ == '__main__':
    AuthApp().run()
