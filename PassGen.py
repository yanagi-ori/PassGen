from tkinter import *


class base:
    def __init__(self):
        self.server = root
        self.server.destroy()
        main_menu()



def startup():
    start_screen = Tk()
    start_screen.title('PassGen - Вход')
    start_screen.update_idletasks()
    s = start_screen.geometry()
    s = s.split('+')
    s = s[0].split('x')
    width_start_screen = int(s[0])
    height_start_screen = int(s[1])
    width = start_screen.winfo_screenwidth()
    height = start_screen.winfo_screenheight()
    width = width // 2
    height = height // 2
    width = width - width_start_screen // 2
    height = height - height_start_screen // 2
    start_screen.geometry('+{}+{}'.format(width, height))

    stsc_main_text = Label(text='Для входа в программу введите ключ шифрования')
    stsc_key = Entry(text='Рекомендуется не оставлять пустым', show='*')
    pw = stsc_key.get()
    stsc_button = Button(text='Вход', command=quit())

    stsc_key.pack()
    stsc_button.pack()
    start_screen.mainloop()


def main_menu():
    menu = Tk()
    menu.title('PassGen')
    menu.mainloop()


root = Tk()
base()