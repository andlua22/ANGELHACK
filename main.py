import subprocess
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests

class LoginApp(App):
    def build(self):
        # UI elements
        layout = BoxLayout(orientation='vertical')
        txt_username = TextInput(text='', multiline=False)
        btn_login = Button(text='Login')
        lbl_result = Label(text='')

        # Event handler for the "Login" button
        def login_on_click(instance):
            username = txt_username.text
            if not username or username == "":
                lbl_result.text = "Need a key"
            else:
                android_id = "your_android_id"  # Replace with your actual code to obtain Android ID
                response = requests.post(
                    "https://defexggxhuligan.000webhostapp.com/vfbsnzjwjw133.php",
                    data={"username": username, "uuid": android_id}
                )
                if response.status_code == 200:
                    if "Login success" in response.text:
                        lbl_result.text = "Login success"
                        # Additional logic on successful login
                    elif "KEY not registered" in response.text:
                        lbl_result.text = "Key invalid"
                    elif "UUID invalid" in response.text:
                        lbl_result.text = "UUID invalid"
                    elif "KEY expired" in response.text:
                        lbl_result.text = "Key expired"
                else:
                    lbl_result.text = "Can't connect to the server."

        btn_login.bind(on_press=login_on_click)

        # Add elements to the screen
        layout.add_widget(Label(text='Enter username:'))
        layout.add_widget(txt_username)
        layout.add_widget(btn_login)
        layout.add_widget(lbl_result)

        return layout

def install_dependencies():
    commands = [
        "sudo apt-get install build-essential",
        "sudo apt-get install libstdc++6",
        "sudo apt-get install aidl"
    ]

    for command in commands:
        subprocess.check_call(command, shell=True)

def run_command(command):
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        raise

def main():
    install_dependencies()
    run_command("buildozer android debug")
    LoginApp().run()

if __name__ == "__main__":
    main()
