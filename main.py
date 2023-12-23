import tkinter
import pyshorteners
def shorten():
    shortner = pyshorteners.Shortener()
    short_url = shortner.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0,short_url))


root = tkinter.Tk()
root.title("URL shortner")
root.geometry("300x300")
longurl_label = tkinter.Label(root, text="Enter your URL")
longurl_entry = tkinter.Entry(root)
shorturl_label = tkinter.Label(root, text="shortened URL")
shorturl_entry =  tkinter.Entry(root)
shorturl_button = tkinter.Button(root, text="Shorten URL", command=shorten)
longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorturl_button.pack()
root.mainloop()
