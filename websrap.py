from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

import tkinter as tk
import tkinter.scrolledtext as st


root = tk.Tk()
root.geometry('500x500+100+100')

value = tk.StringVar()
urlInput = tk.Entry(root, width=100, border=3, fg='red', textvariable=value)
urlInput.pack(ipady=10)



def crawl():
    
 html = urlopen(urlInput.get())
 print(html)
 
 soup = bs(html,'lxml' )
 
 title = soup.prettify()

 code = st.ScrolledText(root,height=100, width=500)
 code.pack()
 code.insert(tk.INSERT, title)
 
 print(title)
 


searchButn = tk.Button(root, text='Crawl', width=50, font=10,pady=5, bg='green', fg='white', command=crawl).pack()





root.mainloop()


