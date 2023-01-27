from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.uix.screen import Screen
import pymysql

class Report(Screen):

    def error(self):
        layout = GridLayout(cols=1, padding=2)
        popuplabel = Label(text="Not Connected to Network")
        closebutton = Button(text="Close", background_color=[1, 1, 1, 1])
        layout.add_widget(popuplabel)
        layout.add_widget(closebutton)
        popup = Popup(title="Load Error...", content= layout, size_hint = (None,None), size=(250, 250))
        popup.open()
        closebutton.bind(on_release=popup.dismiss)

    def show_record(self):
        try:
            mydb = pymysql.connect(
                host="localhost",
                user="root",
                password="password",
                database="mydatabse"
            )
            mycursor = mydb.cursor()
            a = self.ids.number.text
            a = -1 * int(a)

            mycursor.execute(
                "SELECT * FROM data WHERE ( Date <= DATE_ADD(CURDATE(),INTERVAL '%s' MONTH) or Date is Null )" % (
                    int(a)))

            records = mycursor.fetchall()
            site = ''
            No = ''
            date = ''
            date2 = ''
            col = ''
            if len(records) > 0:
                for x in records:
                    site = f'{site}\n{x[0]}'
                    self.ids.location.text = f'{site}'
                    No = f'{No}\n{x[1]}'
                    self.ids.asset.text = f'{No}'
                    col = f'{col}\n{x[5]}'
                    self.ids.tm.text = f'{col}'
                    date = f'{date}\n{x[8]}'
                    self.ids.date.text = f'{date}'
                    date2 = f'{date2}\n{x[11]}'
                    self.ids.date2.text = f'{date2}'
            else:
                self.ids.location.text = site
                self.ids.No.text = No
                self.ids.date.text = date
                self.ids.date2.text = date2

            mycursor.reset()

            mydb.commit()
            mydb.close()
        except pymysql.connect.Error:
            self.error()

