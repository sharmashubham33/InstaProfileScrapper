from tkinter import *
import tkinter as tk    
from urllib.request import urlopen,Request
import io
from bs4 import BeautifulSoup as bs
import requests
from PIL import ImageTk
import PIL.Image


window = Tk()
window.configure(background="white")
window.title("INSTAGRAM PROFILE SCRAPER")

window.geometry("1120x520")
window.iconbitmap('C:/Users/Shubham/Downloads/Instagram_Scrapper-master/Instagram_Scrapper-master/meta/insta.ico')  #path to be added
window.resizable(0,0) # CANNOT RESIZE WINDOW NOW


# SEARCHING USERNAME WITH THE TEXT PROVIDED IN txt2

def search():
    try:
        global img5,user
        user= str(txt2.get())
        req = requests.get('https://www.instagram.com/' + user)
        obj = bs(req.text , 'html.parser')

        # DOWNLOAD DP
        insta_dp = obj.find('meta' , property="og:image")
        insta_dp_url = insta_dp.attrs['content']
        html2 = urlopen(insta_dp_url)
        raw_data = html2.read()
        img5 = PIL.Image.open(io.BytesIO(raw_data))
        img5 = img5.resize((150,150), PIL.Image.ANTIALIAS)

        # FETCH INFO
        user_info = obj.find('meta' , property="og:description")
        user_info_url = user_info.attrs['content'][:40]
        split = user_info_url.split(' ')
        followers = split[0]
        followers = followers.replace('m' , 'M')
        following = split[2]
        posts = split[4]
        followers1 = followers + ' FOLLOWERS'
        following1 = following + ' FOLLOWING'
        posts1 = posts + ' POSTS'
        followers_label.config(text=followers1)
        following_label.config(text=following1)
        posts_label.config(text=posts1)

        # SHOW DP
        image = ImageTk.PhotoImage(img5)
        pannel = Label(window,image=image,borderwidth=0)
        pannel.image = image
        pannel.pack()
        pannel.place(x=885, y=90)

        img4 = PIL.Image.open('C:/Users/Shubham/Downloads/Instagram_Scrapper-master/Instagram_Scrapper-master/meta/download.png')
        img4 = img4.resize((40,40), PIL.Image.ANTIALIAS)
        sp_img4 = ImageTk.PhotoImage(img4)
        pannel2 = Button(window,command=download_img,image = sp_img4,borderwidth=0,bg='white')
        pannel2.image = sp_img4
        pannel2.pack()
        pannel2.place(x=940, y=245)
    except Exception as e:
        print(e)
        error_label = tk.Label(window,text="ID NOT FOUND PLEASE TRY AGAIN",width=30, height=1, fg="white", bg="firebrick1",font=('times', 14, ' bold '))
        error_label.place(x=400, y=250)
        window.after(4000,destroy_widget,error_label)
    
def clear():
    txt2.delete(first=0,last=100)

def download_img():
    img5.save(user+'.jpg')
    pic = tk.Label(window, text="Picture Downloaded!", width=20, height=1, fg="black", bg="gold",font=('times', 14, ' bold '))
    pic.place(x=400, y=250)
    window.after(4000, destroy_widget,pic )



def destroy_widget(widget):
        widget.destroy()

img1 = PIL.Image.open('C:/Users/Shubham/Downloads/Instagram_Scrapper-master/Instagram_Scrapper-master/meta/ig.png')
img1 = img1.resize((200,200) , PIL.Image.ANTIALIAS)
sp_img1 = ImageTk.PhotoImage(img1)
pannel3 = Label(window,image=sp_img1,borderwidth=0,bg='white')
pannel3.pack()
pannel3.place(x=50, y=70)

img2 = PIL.Image.open('C:/Users/Shubham/Downloads/Instagram_Scrapper-master/Instagram_Scrapper-master/meta/search.png')
img2 = img2.resize((40,40), PIL.Image.ANTIALIAS)
sp_img2 = ImageTk.PhotoImage(img2)
pannel4 = Button(window,image=sp_img2,command=search,borderwidth=0,bg='white')
pannel4.pack()
pannel4.place(x=750, y=175)

img3 = PIL.Image.open('C:/Users/Shubham/Downloads/Instagram_Scrapper-master/Instagram_Scrapper-master/meta/eraser.png')
img3 = img3.resize((40,40), PIL.Image.ANTIALIAS)
sp_img3 = ImageTk.PhotoImage(img3)
pannel5 = Button(window, image=sp_img3,command=clear,borderwidth=0,bg='white')
pannel5.pack()
pannel5.place(x=810, y=175)





middle_box = tk.Label(window, text="INSTAGRAM PROFILE SCRAPER" , width=30, height=2, fg='white',bg='maroon2',font=('times', 25 , 'bold'))
middle_box.place(x=274, y=10)

txt = tk.Label(window, text="ENTER YOUR ID",width=18,height=1,fg='white',bg='blue2',font=('times',16,'bold'))
txt.place(x=394, y=120)

txt2 = tk.Entry(window,fg='black',bg='white',width=26,borderwidth=7,font=('times',25,'bold'))
txt2.place(x=280, y=170)

followers_label = tk.Label(window,text="FOLLOWERS",width=17, height=2, fg="white", bg="maroon2",font=('times', 18, ' bold '))
followers_label.place(x=200, y=300)

following_label = tk.Label(window,text="FOLLOWING", width=17,height=2,fg="white",bg="spring green",font=('times',18,'bold'))
following_label.place(x=470, y=300)

posts_label = tk.Label(window, text="POSTS", width=17, height=2, fg="white", bg="dark violet",font=('times', 18, ' bold '))
posts_label.place(x=740, y=300)

window.mainloop()