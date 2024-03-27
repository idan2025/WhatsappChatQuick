import subprocess
import webbrowser
import tkinter as tk
from ttkbootstrap import Style
import ttkbootstrap as tb
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def change_theme(theme_var):
    new_style = Style(theme=theme_var)
    new_style.theme_use()

window = tb.Window(themename="darkly")
window.geometry("695x170")
window.resizable(False, False)
window.configure(bg="#333")
datafile = 'icon.ico'
defaultIMG = resource_path(datafile)
window.wm_iconbitmap(defaultIMG)
window.wm_title('Whatsapp Chat Quick v0.3.0')

style = Style(theme='darkly')

greeting = tb.Label(text="Welcome to Whatsapp Chat Quick")
entry1 = tb.Entry(width=70)
entry2 = tb.Entry(width=20)
entry2.insert(0, "972")
entry2.config(state="disabled")
spacer = tb.Label(window, text="  ", width=1)
label1 = tb.Label(text="Input a Whatsapp number")
label2 = tb.Label(text="Country code: (972/1/Other)")
label3 = tb.Label(text="MIT Licensed | 2024 by Idan Less")

code_list = ["","972", "1", "other"]
version_list = ["","Desktop", "Web"]
themes = ["", "darkly", "cosmo", "cyborg", "flatly", "journal", "lumen", "minty", "pulse", "sandstone", "simplex", "solar", "superhero", "united", "yeti"]

whichversion = tb.StringVar(window)
variable = tb.StringVar(window)
themevar = tb.StringVar(window)
variable.set("972")
whichversion.set("Desktop")
themevar.set("darkly")

def set_entry_state(value):
    if value == "other":
        entry2.config(state="normal")
        entry2.delete(0, 'end')
    else:
        entry2.config(state="normal")
        entry2.delete(0, 'end')
        entry2.insert(0, value)
        entry2.config(state="disabled")

dropdown = tb.OptionMenu(window, variable, *code_list, command=set_entry_state)
version = tb.OptionMenu(window, whichversion, *version_list, bootstyle="success")
theme_choice = tb.OptionMenu(window, themevar, *themes, command=lambda theme: change_theme(theme))

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
    try:
        number = entry1.get()
        first_number = entry1.get()[0]
        if first_number == '0':
            number = number[1:]
        if whichversion.get() == "Desktop":
            isDesktop()
        elif whichversion.get() == "Web":
            isWeb()
        label1.config(text="Input a Whatsapp number")
    except:
        label1.config(text="Invalid number or empty line")

def copy_text(event, entry):
    entry.clipboard_clear()
    entry.clipboard_append(entry.get())

def is_numeric(text):
    # Check if the text contains only numeric characters
    return all(char.isdigit() for char in text)


def process_pasted_text(entry):
    # Get the current text in the Entry widget
    text = entry.get()
    # Remove any empty spaces
    text = text.replace(" ", "")
    # Update the text in the Entry widget
    entry.delete(0, "end")
    entry.insert(0, text)

def paste_text(event, entry):
    # Schedule the processing of pasted text after a short delay
    entry.after(50, lambda: process_pasted_text(entry))

def select_all(event,entry):
    entry.select_range(0, 'end')


menu = tb.Menu(window, tearoff=0)
menu.add_command(label="Copy", command=lambda: copy_text(None, entry1))
menu.add_command(label="Paste", command=lambda: paste_text(None, entry1))
menu.add_command(label="Select All", command=lambda: select_all(None, entry1))
entry1.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))
entry1.bind("<Control-v>", lambda event: paste_text(event, entry1))
entry1.bind("<Control-c>", lambda event: copy_text(event, entry1))
entry1.bind("<Control-a>", lambda event: select_all(event, entry1))

menu2 = tb.Menu(window, tearoff=0)
menu2.add_command(label="Copy", command=lambda: copy_text(None, entry2))
menu2.add_command(label="Paste", command=lambda: paste_text(None, entry2))
menu2.add_command(label="Select All", command=lambda: select_all(None, entry2))
entry2.bind("<Button-3>", lambda event: menu2.post(event.x_root, event.y_root))
entry2.bind("<Control-c>", lambda event: copy_text(event, entry2))
entry2.bind("<Control-v>", lambda event: paste_text(event, entry2))
entry1.bind("<Control-a>", lambda event: select_all(event, entry2))

image = Image.open(defaultIMG)
photo = ImageTk.PhotoImage(image)
img_label = tb.Label(image=photo)
img_label.image = photo
button = tb.Button(text="Open Whatsapp chat", command=OnButtonpress, bootstyle="success,toolbutton")

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

# Theme menu

theme_choice.grid(row=5, column=2)

window.mainloop()
