from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
import pymysql.connections

''' Adding Method to building 901 
    with help of location and asset number
    '''

class Add_Update(Screen):
    def pop_add(self):
        layout = GridLayout(cols=1, padding=2)
        popuplabel = Label(text="Invalid Number\n"
                                "Number already exists \n"
                                "Re- Enter the asset Number..\n")
        closebutton = Button(text="Close", background_color=[1, 1, 1, 1])
        layout.add_widget(popuplabel)
        layout.add_widget(closebutton)
        popup = Popup(title="Add Error...", content=layout, size_hint=(None, None), size=(500, 500))
        self.clear()
        popup.open()
        closebutton.bind(on_release=popup.dismiss)

    def pop_update(self):
        layout = GridLayout(cols=1, padding=2)
        popuplabel = Label(text="Date is similar")
        closebutton = Button(text="Close",  background_color=[1, 1, 1, 1])
        layout.add_widget(popuplabel)
        layout.add_widget(closebutton)
        popup = Popup(title="Note...", content=layout, size_hint=(None, None), size=(250, 250))
        popup.open()
        closebutton.bind(on_release=popup.dismiss)

    def pop_load(self):
        layout = GridLayout(cols=1, padding=2)
        popuplabel = Label(text="Check the range of the No")
        closebutton = Button(text="Close", background_color=[1, 1, 1, 1])
        layout.add_widget(popuplabel)
        layout.add_widget(closebutton)
        popup = Popup(title="Load Error...", content= layout, size_hint = (None,None), size=(250, 250))
        self.clear()
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

    def equals(self):
        try:
            mydb = pymysql.connect(
                host="localhost",
                user="root",
                password="password",
                database="mydatabse"
            )

            mycursor = mydb.cursor()
            a = self.ids.c1.text.strip()
            b = self.ids.c2.text.strip()
            c = self.ids.c3.text.strip()
            d = self.ids.c4.text.strip()
            e = self.ids.c5.text.strip()
            f = self.ids.c6.text.strip()
            g = self.ids.c7.text.strip()
            h = self.ids.c8.text.strip()
            i = self.ids.c9.text.strip()
            j = self.ids.c10.text
            k = self.ids.c11.text

            flag = 0

            if i == "Null" or int(b) == 0:
                mycursor.execute("SELECT No FROM data")
                for x in mycursor:
                    for y in x:
                        if int(y) == int(b) or int(b) == 0:
                            flag = 1
                            break
                if (flag == 0):
                    mycursor.execute(
                        "INSERT INTO data(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11) "
                        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,Null,%s,%s)",
                        (a, b, c, d, e, f, g, h, j, k))
            else:
                mycursor.execute("SELECT No FROM data")
                for qw in mycursor:
                    for qwe in qw:
                        if int(qwe) == int(b) or int(b) == 0:
                            flag = 1
                            break
                if (flag == 0):
                    mycursor.execute(
                        "INSERT INTO data(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11) "
                        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (a, b, c, d, e, f, g, h, i, j, k))

            if (flag == 1):
                self.pop_add()
            mydb.commit()
            mydb.close()

        except pymysql.Connect.Error:
            self.error()
    pass

    def load_data(self):
        try:
            mydb = pymysql.connect(
                host="localhost",
                user="root",
                password="password",
                database="mydatabse"
            )
            mycursor = mydb.cursor()
            a = self.ids.c2.text
            b = self.ids.c1.text
            flag = 0
            mycursor.execute("SELECT No FROM data ")

            for y in mycursor:
                for i in y:
                    if(i==int(a)):
                        mycursor.execute("SELECT * FROM data WHERE "
                                         "No = '%s' "
                                         "AND "
                                         "c1 = '%s' " % (a, b))
                        date = ''
                        for x in mycursor:
                            self.ids.c3.text = x[2]
                            self.ids.c4.text = x[3]
                            self.ids.c5.text = x[4]
                            self.ids.c6.text = x[5]
                            self.ids.c7.text = x[6]
                            self.ids.c8.text = x[7]
                            date = f'{date}\n{x[8]}'
                            self.ids.c9.text = f'{date}'
                            self.ids.c10.text = x[9]
                            self.ids.c11.text = x[10]
                            flag = 1
                            break

            if(flag == 0):
                self.pop_load()
                self.ids.c2.text = '0'

            mydb.commit()
            mydb.close()
        except pymysql.connect.Error:
            print()


    def update(self):
        try:
            mydb = pymysql.connect(
                host="localhost",
                user="root",
                password="password",
                database="mydatabse"
            )
            mycursor = mydb.cursor()

            a = self.ids.c1.text.strip()
            b = self.ids.c2.text.strip()
            c = self.ids.c3.text.strip()
            d = self.ids.c4.text.strip()
            e = self.ids.c5.text.strip()
            f = self.ids.c6.text.strip()
            g = self.ids.c7.text.strip()
            h = self.ids.c8.text.strip()
            i = self.ids.c9.text.strip()
            j = self.ids.c10.text
            k = self.ids.c11.text
            print(i)
            date = ''
            if int(a) > 0:
                mycursor.execute("SELECT c8 FROM data WHERE c2 = '%s' " % (a))
                for x in mycursor:
                    date = f'{date}{x[0]}'
                    if date == i:
                        mycursor.execute(
                            "UPDATE data SET c3 = '%s', "
                            "c4= '%s', "
                            "c5= '%s', "
                            "c6= '%s',"
                            "c7= '%s', "
                            "c9 = '%s', "
                            "c10= '%s', "
                            "c11= '%s'"
                            " WHERE c2 = '%s' " % (
                                c, d, e, f, g, h, j, k, a))
                        self.pop_update()
                    elif (date != i):
                        mycursor.execute("UPDATE data SET date4 = date3 WHERE c2 = '%s' " % (a))
                        mycursor.execute("UPDATE data SET date3 = date2 WHERE c2 = '%s' " % (a))
                        mycursor.execute("UPDATE data SET date2 = c8 WHERE c2 = '%s' " % (a))
                        mycursor.execute("UPDATE data SET c8 = '%s' WHERE c2 = '%s' " % (i, a))

            mydb.commit()
            mydb.close()
        except pymysql.connect.Error:
            self.error()
    def clear(self):
        self.ids.c2.text = "0"
        self.ids.c3.text = ""
        self.ids.c4.text = ""
        self.ids.c5.text = ""
        self.ids.c6.text = ""
        self.ids.c7.text = ""
        self.ids.c8.text = "Null"
        self.ids.c9.text = ""
        self.ids.c10.text = ""
        self.ids.c11.text = ""
        pass




















