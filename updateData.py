from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager , Screen
import mysql.connector

class Update_901(Screen):

    def pop(self):
        layout = GridLayout(cols=1, padding=2)

        popuplabel = Label(text="Check the asset number \n"
                                "Range: 3000-4000 \n"
                                "Number Don't exists..")
        closebutton = Button(text="Close", font_size=20, background_color=[1, 1, 1, 1])
        layout.add_widget(popuplabel)
        layout.add_widget(closebutton)
        popup = Popup(title="Error...", content= layout, size_hint = (None,None), size=(250, 250))
        self.clear()
        popup.open()
        closebutton.bind(on_release=popup.dismiss)

    def pop_update(self):
        layout = GridLayout(cols=1, padding=2)

        popuplabel = Label(text="Backup date is similar as last date.. ")
        closebutton = Button(text="Close", font_size=20, background_color=[1, 1, 1, 1])
        layout.add_widget(popuplabel)
        layout.add_widget(closebutton)
        popup = Popup(title="Error...", content= layout, size_hint = (None,None), size=(250, 250))
        popup.open()
        closebutton.bind(on_release=popup.dismiss)

    def load_data(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="bSK84*5y",
            database="MyApp"
        )
        mycursor = mydb.cursor()
        a = self.ids.asset.text
        b = self.ids.Location.text
        flag = 0
        mycursor.execute("SELECT asset FROM data ")

        for y in mycursor:
            for i in y:
                if(i==int(a)):
                    mycursor.reset()
                    mycursor.execute("SELECT * FROM data WHERE asset = '%s' AND Location = '%s' " % (a, b))
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

        if(flag == 0):
            self.pop()
            self.ids.asset.text = '0'

        mydb.commit()
        mydb.close()


    def update(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="bSK84*5y",
            database="MyApp"
        )
        mycursor = mydb.cursor()

        b = self.ids.Location.text.strip()
        a = self.ids.asset.text.strip()
        c = self.ids.Device_Name.text.strip()
        d = self.ids.MAC_Address.text.strip()
        e = self.ids.Service_No.text.strip()
        f = self.ids.Team_Viewer.text.strip()
        g = self.ids.Web_root.text.strip()
        h = self.ids.ease_US.text.strip()
        i = self.ids.Last_BackUp.text.strip()
        j = self.ids.Comments.text.strip()
        k = self.ids.Notes.text.strip()

        date = ''
        if int(a) > 0:
            mycursor.reset()

            mycursor.execute("SELECT Last_Backup FROM data WHERE asset = '%s' " % (a))
            for x in mycursor:
                date = f'{date}{x[0]}'
                if date == i:
                    mycursor.reset()
                    mycursor.execute(
                        "UPDATE data SET Device_Name = '%s', MAC_address= '%s', Service_No= '%s', Team_Viewer= '%s', Web_root= '%s', ease_US = '%s', Comments= '%s', Notes= '%s' WHERE asset = '%s' " % (
                            c, d, e, f, g, h, j, k, a))
                    self.pop_update()
                elif (date != i):
                    mycursor.reset()
                    mycursor.execute("UPDATE data SET date_4 = date_3 WHERE asset = '%s' " % (a))
                    mycursor.reset()
                    mycursor.execute("UPDATE data SET date_3 = date_2 WHERE asset = '%s' " % (a))
                    mycursor.reset()
                    mycursor.execute("UPDATE data SET date_2 = Last_Backup WHERE asset = '%s' " % (a))
                    mycursor.reset()
                    mycursor.execute("UPDATE data SET Last_Backup = '%s' WHERE asset = '%s' " % (i,a))
        mydb.commit()
        mydb.close()

    def clear(self):
        self.ids.asset.text = "0"
        self.ids.Device_Name.text = ""
        self.ids.MAC_Address.text = ""
        self.ids.Service_No.text = ""
        self.ids.Team_Viewer.text = ""
        self.ids.Web_root.text = ""
        self.ids.ease_US.text = ""
        self.ids.Last_BackUp.text = ""
        self.ids.Comments.text = ""
        self.ids.Notes.text = ""
        pass




class Update_3601(Screen):
    def pop(self):
        layout = GridLayout(cols=1, padding=2)
        popuplabel = Label(text="Check the asset number \n"
                                "Range: 3000-4000 \n"
                                "Number Don't exists..")
        closebutton = Button(text="Close", font_size=20, background_color=[1, 1, 1, 1])
        layout.add_widget(popuplabel)
        layout.add_widget(closebutton)
        popup = Popup(title="Error...", content= layout, size_hint = (None,None), size=(250, 250))
        self.clear()
        popup.open()
        closebutton.bind(on_release=popup.dismiss)

    def load_data(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="bSK84*5y",
            database="MyApp"
        )
        mycursor = mydb.cursor()
        a = self.ids.asset.text
        b = self.ids.Location.text
        flag = 0
        mycursor.execute("SELECT asset FROM data ")

        for y in mycursor:
            for i in y:
                if(i==int(a)):
                    print("found")
                    mycursor.reset()
                    mycursor.execute("SELECT * FROM data WHERE asset = '%s' " % (a))
                    date = ''
                    for x in mycursor:
                        print(x)
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

        if(flag == 0):
            self.pop()
            self.ids.asset.text = '0'
        mydb.commit()
        mydb.close()

    def update(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="bSK84*5y",
            database="MyApp"
        )
        mycursor = mydb.cursor()
        b = self.ids.Location.text
        a = self.ids.asset.text
        c = self.ids.Device_Name.text
        d = self.ids.MAC_Address.text
        e = self.ids.Service_No.text
        f = self.ids.Team_Viewer.text
        g = self.ids.Web_root.text
        h = self.ids.ease_US.text
        i = self.ids.Last_BackUp.text
        j = self.ids.Comments.text
        k = self.ids.Notes.text

        if (int(a) >0 ):
            mycursor.execute( "UPDATE data SET Device_Name = '%s', MAC_address= '%s', Service_No= '%s', Team_Viewer= '%s', Web_root= '%s', ease_US = '%s', Last_Backup= '%s', Comments= '%s', Notes= '%s' WHERE asset = '%s' " % (c,d,e,f,g,h,i,j,k,a) )
            for x in mycursor:
                print(x)
        else:
            print("x")

        mydb.commit()
        mydb.close()

    def clear(self):
        self.ids.asset.text = ""
        self.ids.Device_Name.text = ""
        self.ids.MAC_Address.text = " "
        self.ids.Service_No.text = " "
        self.ids.Team_Viewer.text = " "
        self.ids.Web_root.text = " "
        self.ids.ease_US.text = " "
        self.ids.Last_BackUp.text = " "
        self.ids.Comments.text = " "
        self.ids.Notes.text = " "
        pass
