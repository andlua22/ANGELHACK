from kivy.app import App
from kivy.uix.button import Button

class SimpleKivyApp(App):
    def build(self):
        return Button(text='Hello Kivy!')

if __name__ == '__main__':
    SimpleKivyApp().run()
