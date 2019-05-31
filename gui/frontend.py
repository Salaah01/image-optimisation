from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class HomePage(GridLayout):

    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)


class Main(App):
    def build(self):
        self.load_kv('frontend.kv')
        return HomePage()


if __name__ == '__main__':
    Main().run()