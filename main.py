import os
from datetime import datetime
from tkinter import *
from ctypes  import *

# TODO Один файл в неделю/месяц
# TODO Доработка GUI, сделать более приятный дизайн.

width = windll.user32.GetSystemMetrics(0) / 4 - 50
height = windll.user32.GetSystemMetrics(1) / 4 - 50

root = Tk()
root.geometry('700x500+{0}+{1}'.format(int(width), int(height)))
root.title('Todo list')
root['bg'] = 'white'

date = datetime.today()
today = '{0}.{1}.{2}'.format(date.year, date.month, date.day )
tommorow = '{0}.{1}.{2}'.format(date.year, date.month, date.day + 1)

def task_today(today, root):
    try:
        i = 1
        with open('tasks\\' + today + '.txt', encoding='UTF-8') as f:
            f_read = f.readlines()
            for line in f_read:
                task = str(i) + '. ' + line
                i = int(i)
                i += 1
                lab = Label(root, font='Airal 12', bg='white', text=task)
                lab.pack()
        new_task(today, width, height)
    except FileNotFoundError:
        lab = Label(root, font='Airal 14', text='Задач на сегодня нет\n\n')
        lab.pack()
        new_task(today, width, height)
def new_task(today, width, height):
    text_task = Text(root, height=7, width=300, font='Arial 14', wrap=WORD)
    text_task.pack()
    def add_task():
        task = text_task.get('1.0', END)
        if task == '\n':
            error_win = Tk()
            error_win.geometry('100x100+{0}+{1}'.format(int(width), int(height)))
            error_win.title('Ошибка')
            error = Label(error_win, text='Задача\n не может быть пустой')
            ok_added = Button(error_win, text='Оk', command=error_win.destroy)
            text_task.delete('1.0', END)
            ok_added.pack()
            error.pack()
            error_win.mainloop()
        else:
            try:
                with open('tasks\\' + tommorow + '.txt', 'a', encoding='UTF-8') as f:
                    f.write(task)
            except FileNotFoundError:
                os.mkdir('tasks')
                with open('tasks\\' + tommorow + '.txt', 'a', encoding='UTF-8') as f:
                    f.write(task)
            task_add = Tk()
            task_add.geometry('100x100+{0}+{1}'.format(int(width), int(height)))
            task_add.title('Ok')
            added = Label(task_add, text='Задача добавлена')
            ok_added = Button(task_add, text='Оk', command=task_add.destroy)
            text_task.delete('1.0', END)
            ok_added.pack()
            added.pack()
            task_add.mainloop()
    btn = Button(root, text='Добавить задачу', command=add_task)
    btn.pack()
    root.mainloop()

task_today(today, root)
root.mainloop()