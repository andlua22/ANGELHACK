from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests

class LoginApp(App):
    def build(self):
        # UI элементы
        layout = BoxLayout(orientation='vertical')
        txt_username = TextInput(text='', multiline=False)
        btn_login = Button(text='Login')
        lbl_result = Label(text='')

        # Обработчик события для кнопки "Login"
        def login_on_click(instance):
            username = txt_username.text
            if not username or username == "":
                lbl_result.text = "Need a key"
            else:
                android_id = "your_android_id"  # Замените на ваш фактический код для получения Android ID
                response = requests.post(
                    "https://defexggxhuligan.000webhostapp.com/vfbsnzjwjw133.php",
                    data={"username": username, "uuid": android_id}
                )
                if response.status_code == 200:
                    if "Login success" in response.text:
                        lbl_result.text = "Login success"
                        # Дополнительная логика при успешном входе
                    elif "KEY not registered" in response.text:
                        lbl_result.text = "Key invalid"
                    elif "UUID invalid" in response.text:
                        lbl_result.text = "UUID invalid"
                    elif "KEY expired" in response.text:
                        lbl_result.text = "Key expired"
                else:
                    lbl_result.text = "Can't connect to server."

        btn_login.bind(on_press=login_on_click)

        # Добавление элементов на экран
        layout.add_widget(Label(text='Enter username:'))
        layout.add_widget(txt_username)
        layout.add_widget(btn_login)
        layout.add_widget(lbl_result)

        return layout

if __name__ == '__main__':
    LoginApp().run()
