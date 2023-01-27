from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

''' Importing Files python class
            access the screens...'''
from report import Report_901
from add import Add_Update_901
from viewdata import ViewData_901

from report import Report_3601
from add import Add_Update_3601
from viewdata import ViewData_3601

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