import subprocess
import webbrowser
import tkinter as tk
from PIL import Image, ImageTk
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


window = tk.Tk()
window.geometry("680x150")
window.resizable(False, False)
window.configure(bg="#333")
datafile = 'icon.ico'
defaultIMG = resource_path(datafile)
window.wm_iconbitmap(defaultIMG)
window.wm_title('Whatsapp Chat Quick v2.0')
greeting = tk.Label(
    fg="white", text="Welcome to Whatsapp Chat Quick", bg="#333")
entry1 = tk.Entry(fg="white", bg="#333", width=70)
entry2 = tk.Entry(fg="white", bg="#333", width=20)
entry2.insert(0, "972")
entry2.config(state="disabled")
entry2.delete(0, 'end')
spacer = tk.Label(window, text="  ", width=1, bg="#333")
label1 = tk.Label(fg="white", bg="#333", text="Input a Whatsapp number")
label2 = tk.Label(fg="white", bg="#333", text="Country code: (972/1/Other)")
label3 = tk.Label(fg="white", bg="#333",
                  text="MIT Licensed | 2023 by Idan Less")

code_list = ["972", "1", "other"]
version_list = ["Desktop", "Web"]
whichversion = tk.StringVar(window)
variable = tk.StringVar(window)
variable.set("972")
whichversion.set("Desktop")


def set_entry_state(value):
    if value == "other":
        entry2.config(state="normal")
        entry2.delete(0, 'end')
    else:
        entry2.config(state="normal")
        entry2.delete(0, 'end')
        entry2.insert(0, value)
        entry2.config(state="disabled")
        entry2.update()


dropdown = tk.OptionMenu(window, variable, *code_list, command=set_entry_state)
version = tk.OptionMenu(window, whichversion, *version_list)


def isDesktop():
    countrycode = entry2.get()
    number = entry1.get()
    subprocess.Popen(
        [f"cmd", "/C", "start whatsapp://send?phone={}{}".format(countrycode, number)], shell=True)


def isWeb():
    number = entry1.get()
    countrycode = entry2.get()
    url = f"https://api.whatsapp.com/send?phone={countrycode}{number}"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)


def OnButtonpress():
    number = entry1.get()
    first_number = entry1.get()[0]
    if first_number == '0':
        number = number[1:]
    if whichversion.get() == "Desktop":
        isDesktop()
    elif whichversion.get() == "Web":
        isWeb()


def copy_text(event, entry):
    entry.clipboard_clear()
    entry.clipboard_append(entry.get())


def paste_text(event, entry):
    entry.insert(0, entry.clipboard_get())


menu = tk.Menu(window, tearoff=0)
menu.add_command(label="Copy", command=lambda: copy_text(None, entry1))
menu.add_command(label="Paste", command=lambda: paste_text(None, entry1))
entry1.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))

menu2 = tk.Menu(window, tearoff=0)
menu2.add_command(label="Copy", command=lambda: copy_text(None, entry2))
menu2.add_command(label="Paste", command=lambda: paste_text(None, entry2))
entry2.bind("<Button-3>", lambda event: menu2.post(event.x_root, event.y_root))


image = Image.open(defaultIMG)
photo = ImageTk.PhotoImage(image)
img_label = tk.Label(image=photo, bg="#333")
img_label.image = photo
button = tk.Button(window, fg="white", bg="Green",
                   text="Open Whatsapp chat", command=OnButtonpress)
window.bind('<Return>', lambda event: OnButtonpress())


greeting.grid(row=0, column=1)
version.grid(row=0, column=2)
img_label.grid(row=0, column=0)
label1.grid(row=1, column=1)
label2.grid(row=1, column=0)
entry1.grid(row=3, column=1)
dropdown.grid(row=2, column=0)
spacer.grid(row=4, column=0)
entry2.grid(row=3, column=0)
label3.grid(row=5, column=0)
button.grid(row=5, column=1)


window.mainloop()
