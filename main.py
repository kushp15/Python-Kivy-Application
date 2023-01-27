from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp


from kivy.core.window import Window

Window.keyboard_anim_args = {'d': .2, 't': 'linear'}
Window.softinput_mode = "below_target"

class MainWindow(Screen):
    pass
class First(Screen):
    pass
class WindowManager(ScreenManager):
    pass

class MyApp(MDApp):
    def build(self):
        kv = Builder.load_file('main.kv')
        return kv

if __name__ == "__main__":
    MyApp().run()