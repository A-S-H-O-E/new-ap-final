from email import message
from msilib import text
from tkinter import *
import requests
from tkinter import messagebox
root = Tk()
root.title('News App')
root.geometry('600x450')
root.configure(background='lightgreen')


def fetchcc():
    country = countryn.get()
    response = requests.get('https://api.printful.com/countries')
    data = response.json()
    results = data['result']
    cc = ''
    for r in results:
        if(r['name'].lower() == country.lower()):
            cc = r['code'].lower()
    if(cc == ''):
        news['text'] = ''
        messagebox.showerror('Error', 'country not found {}'.format(country))
    else:
        fetchnews(cc)


def fetchnews(cc):
    print(cc)
    link = 'https://newsapi.org/v2/top-headlines?country=' + \
        cc+'&apiKey=bdc912d442614e15846f1804f1b751d8'
    response = requests.get(link)
    data = response.json()
    articles = data['articles']
    headlines = ''
    counter = 1
    for a in articles:
        headlines = headlines + str(counter) + '. ' + a['title'] +'\n'
        counter = counter + 1
    if(headlines == ''):
        messagebox.showerror('Error','No news found')
    else:
        news['text'] = headlines
    
header = Label(root, text='Entry country name for news',
font=('Times 20 bold', 18))
header.place(x=140, y=40)
countryn = StringVar()
country_entry = Entry(root, textvariable=countryn)
country_entry.place(x=230, y=120)
srcbutn = Button(root, text='Search', font='Times 20 bold',
height=1, width=6, command=lambda: fetchcc())
srcbutn.place(x=235, y=180)
news = Label(root,text = '', bg = 'white', fg = 'black',font=('Times 20 bold',16))
news.place(x=190, y = 260)
root.mainloop()
