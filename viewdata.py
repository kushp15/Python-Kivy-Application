from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager , Screen
import pymysql

class ViewData_901(Screen):

    def pop(self):
        layout = GridLayout(cols=1, padding=2)

        popuplabel = Label(text="Check the asset number \n"
                                "Range: 3000-4000 \n"
                                "Number Don't exists..")
        closebutton = Button(text="Close", font_size=20, background_color=[1, 1, 1, 1])
        layout.add_widget(popuplabel)
        layout.add_widget(closebutton)
        popup = Popup(title="Error...", content= layout, size_hint = (None,None), size=(250, 250))
        popup.open()
        closebutton.bind(on_release=popup.dismiss)

    def error(self):
        layout = GridLayout(cols=1, padding=2)
        popuplabel = Label(text="Not Connected to Network")
        closebutton = Button(text="Close", background_color=[1, 1, 1, 1])
        layout.add_widget(popuplabel)
        layout.add_widget(closebutton)
        popup = Popup(title="Load Error...", content= layout, size_hint = (None,None), size=(250, 250))
        popup.open()
        closebutton.bind(on_release=popup.dismiss)

    def load_data(self):
        try:
            mydb = pymysql.connect(
                host="192.168.1.10",
                user="admin",
                password="bSK84*5y",
                database="myapp"
            )
            mycursor = mydb.cursor()
            a = self.ids.asset.text
            b = self.ids.Location.text
            flag = 0
            mycursor.execute("SELECT asset FROM data ")

            for y in mycursor:
                for i in y:
                    if (i == int(a)):
                        mycursor.execute("SELECT * FROM data WHERE "
                                         "asset = '%s' "
                                         "AND "
                                         "Location = '%s' " % (a, b))
                        date = ''
                        for x in mycursor:
                            self.ids.Device_Name.text = x[2]
                            self.ids.MAC_Address.text = x[3]
                            self.ids.Service_No.text = x[4]
                            self.ids.Team_Viewer.text = x[5]
                            self.ids.Web_root.text = x[6]
                            self.ids.ease_US.text = x[7]
                            date = f'{date}\n{x[8]}'
                            self.ids.Last_BackUp.text = f'{date}'
                            self.ids.Comments.text = x[9]
                            self.ids.Notes.text = x[10]
                            flag = 1
                            break

            if (flag == 0):
                self.pop_load()
                self.ids.asset.text = '0'

            mydb.commit()
            mydb.close()
        except pymysql.connect.Error:
            self.error()


class ViewData_3601(Screen):

    def pop(self):
        layout = GridLayout(cols=1, padding=2)

        popuplabel = Label(text="Check the asset number \n"
                                "Range: 1001-2000 \n"
                                "Number Don't exists..")
        closebutton = Button(text="Close", font_size=20, background_color=[1, 1, 1, 1])
        layout.add_widget(popuplabel)
        layout.add_widget(closebutton)
        popup = Popup(title="Error...", content= layout, size_hint = (None,None), size=(250, 250))
        popup.open()
        closebutton.bind(on_release=popup.dismiss)

    def error(self):
        layout = GridLayout(cols=1, padding=2)
        popuplabel = Label(text="Not Connected to Network")
        closebutton = Button(text="Close", background_color=[1, 1, 1, 1])
        layout.add_widget(popuplabel)
        layout.add_widget(closebutton)
        popup = Popup(title="Load Error...", content= layout, size_hint = (None,None), size=(250, 250))
        popup.open()
        closebutton.bind(on_release=popup.dismiss)

    def load_data(self):
        try:
            mydb = pymysql.connect(
                host="192.168.1.10",
                user="admin",
                password="bSK84*5y",
                database="myapp"
            )
            mycursor = mydb.cursor()
            a = self.ids.asset.text
            b = self.ids.Location.text
            flag = 0
            mycursor.execute("SELECT asset FROM data ")

            for y in mycursor:
                for i in y:
                    if (i == int(a)):
                        mycursor.execute("SELECT * FROM data WHERE "
                                         "asset = '%s' "
                                         "AND "
                                         "Location = '%s' " % (a, b))
                        date = ''
                        for x in mycursor:
                            self.ids.Device_Name.text = x[2]
                            self.ids.MAC_Address.text = x[3]
                            self.ids.Service_No.text = x[4]
                            self.ids.Team_Viewer.text = x[5]
                            self.ids.Web_root.text = x[6]
                            self.ids.ease_US.text = x[7]
                            date = f'{date}\n{x[8]}'
                            self.ids.Last_BackUp.text = f'{date}'
                            self.ids.Comments.text = x[9]
                            self.ids.Notes.text = x[10]
                            flag = 1
                            break

            if (flag == 0):
                self.pop_load()
                self.ids.asset.text = '0'

            mydb.commit()
            mydb.close()
        except pymysql.connect.Error:
            self.error()