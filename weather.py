from tkinter import *
from tkinter import ttk

import requests

def data_get():
    city = city_name.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    try:
        w_lable1.config(text=data['weather'][0]['main'])
        wb_lable1.config(text=data['weather'][0]['description'])
        temp_lable1.config(text=str(round(data['main']['temp'] - 273.15, 2)) + " °C")
        per_lable1.config(text=str(data['main']['pressure']) + " hPa")
    except KeyError:
        w_lable1.config(text="N/A")
        wb_lable1.config(text="Invalid City")
        temp_lable1.config(text="N/A")
        per_lable1.config(text="N/A")



win= Tk()
win.title("WHEATHER APP")
win.config(bg="pink")
win.geometry("500x570")

name_lable = Label(win,text="wheather app",font=("time new roman",35,"bold"))

name_lable.place(x=25,y=50,height=50,width=450)

list_name=["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat",
           "Haryana","Himachal Pradesh","Jharkhand""Karnataka","Kerala","Madhya Pradesh","Maharashtra",
            "Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu",
            "Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]

city_name=StringVar()
com = ttk.Combobox(win,text="wheather app", value= list_name,font=("time new roman",25,"bold"),textvariable=city_name)

com.place(x=25,y=120,height=50,width=450)



w_lable = Label(win,text="wheather climate",font=("time new roman",20))
w_lable.place(x=25,y=260,height=50,width=210)

w_lable1 = Label(win,text="..",font=("time new roman",20))
w_lable1.place(x=250,y=260,height=50,width=210)


wb_lable = Label(win,text="wheather Discription",font=("time new roman",17))
wb_lable.place(x=25,y=330,height=50,width=210)


wb_lable1 = Label(win,text="..",font=("time new roman",17))
wb_lable1.place(x=250,y=330,height=50,width=210)


temp_lable = Label(win,text="Tempreature",font=("time new roman",20))
temp_lable.place(x=25,y=400,height=50,width=210)

temp_lable1 = Label(win,text="..",font=("time new roman",20))
temp_lable1.place(x=250,y=400,height=50,width=210)



per_lable = Label(win,text="Pressure",font=("time new roman",20))
per_lable.place(x=25,y=470,height=50,width=210)

per_lable1 = Label(win,text="..",font=("time new roman",20))
per_lable1.place(x=250,y=470,height=50,width=210)


done_button=Button(win,text="Done",font=("Time new roman",20,"bold"),command=data_get)

done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()



