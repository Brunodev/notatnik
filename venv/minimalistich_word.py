import os
import pynput
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.filedialog import *

def press(key):
    if key == pynput.keyboard.Key.f4:
        quit()
    #if key == pynput.keyboard.Key.f5:
        #new_file()
    if key == pynput.keyboard.Key.f2:
        open_file()
    if key == pynput.keyboard.Key.f1:
        save()
        print("dsdas")

pynput.keyboard.Listener(on_press=press).start()

def new_file():
    text_area.delete(1.0, END)

def open_file():
    file = askopenfile(filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    try:
        text_area.delete("1.0", END)
        text_area.insert("1.0", file.read())
    except Exception:
        print("Couldn't read file")

def save():
    contents = text_area.get(1.0,"end-1c") #store the contents of the text widget in a str
    try:                                       #this try/except block checks to
        with open(file, 'w') as outputFile:  #see if the str containing the output
            outputFile.write(contents)         #file (self.f) exists, and we can write to it,
    except AttributeError:                     #and if it doesn't,
        self.save_as()

def save_file_as():
    file = filedialog.asksaveasfilename(initialfile='unknown.txt',
                                        defaultextension=".txt",
                                        filetypes=(
                                            ('text files', '*.txt'),
                                            ('All files', '*.*')
                                        )
                                        )
    file = open(file, "w")
    file.write(text_area.get(1.0, END))



def quit():
    window.destroy()

window =Tk()
window.title("Minimalistic word")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width,
                                     window_height, x,y ))

font_name = StringVar(window)
font_name.set("Source Sans Pro") #zmienić font

font_size = StringVar(window)
font_size.set("19")

font_color = StringVar(window)
font_color.set("#e8e3e3")

bg_color = StringVar(window)
bg_color.set("#202124")

text_area = Text(window, font=(font_name.get(), font_size.get()),bg=bg_color.get(), fg=font_color.get(), insertbackground=font_color.get(), relief="flat")
window['bg'] = bg_color.get()

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=2)
text_area.grid(row=0, column=0, sticky = N + E + S + W,  padx=window_width, pady=80)


a = True
window.attributes("-fullscreen", a)

frame = Frame()
frame.grid()

window.mainloop()