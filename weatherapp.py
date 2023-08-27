import requests
from bs4 import BeautifulSoup
from tkinter import *
from PIL import Image,ImageTk

url="https://weather.com/en-IN/weather/today/l/6ecbadd5ca4ce6c97d16802065235a0e2d6f88cb05cd22dd3fe0fb1da4df330c"
root=Tk()
root.title("Weather App")
root.config(bg="white")
root.geometry("670x300")

def getweather():
    response=requests.get(url)
    data=BeautifulSoup(response.content,'html.parser')
    location=data.find('h1',class_="CurrentConditions--location--1YWj_").text
    temparature=data.find('span',class_="CurrentConditions--tempValue--MHmYY").text
    weatherprediction=data.find('div',class_="CurrentConditions--phraseValue--mZC_p").text
    loc_label.config(text=location)
    temp_label.config(text=temparature)
    weatherpred_label.config(text=weatherprediction)

    temp_label.after(30000,getweather)
    root.update()
    
    

img=Image.open("download1.jpeg")
#resize_img=img.resize((200,200),Image.LANCZOS)
photo1=ImageTk.PhotoImage(img)
label_photo1=Label(image=photo1)
label_photo1.place(x=370,y=20)

loc_label=Label(root,font="calibri 20 bold",bg="white")
loc_label.grid(row=0,sticky="N",padx=120)
temp_label=Label(root,font="calibri 60 bold",bg="white")
temp_label.grid(row=3,sticky="W",padx=50)
weatherpred_label=Label(root,font="calibri 20 bold",bg='white')
weatherpred_label.grid(row=4,sticky=W,padx=50)
getweather()


#Label(root,image=img,bg="white").grid(row=1,sticky="E")


root.mainloop()

