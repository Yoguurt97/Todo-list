import os
from datetime import datetime
from tkinter import *
from ctypes  import *

# TODO Один файл в неделю/месяц
# TODO Доработка GUI, сделать более приятный дизайн.
# TODO Дописать удаление задач, инфу о программе(версия, хелпа)

# Получение разешения экрана пользователя
width = windll.user32.GetSystemMetrics(0) / 4 - 50
height = windll.user32.GetSystemMetrics(1) / 4 - 50
# Создание окна
root = Tk()
root.geometry('700x500+{0}+{1}'.format(int(width), int(height)))
root.title('Todo list')
root['bg'] = 'white'


def m_delete_task():
    win_delete = Tk()
    win_delete.geometry('300x120+{0}+{1}'.format(int(width), int(height)))
    area = Label(win_delete, text='Введите дату задачи, \nкоторую хотите удалить(ГГГГ.ММ.Д)\n')
    value = Entry(win_delete)
    def delete_task():
        try:
            date_task = value.get()
            name_file = value.get()
            os.remove('tasks\\{}'.format(name_file))
            value.delete('0', END)
        except FileNotFoundError:
            value.delete('0', END)
    def delete_all_task():
        listdir = os.listdir('tasks\\')
        for file in listdir:
            os.remove('tasks\\' + file)
        value.delete('0', END)
    btn_delete_all = Button(win_delete, text='Удалить все задачи', command=delete_all_task).pack(side='bottom')
    btn_delete = Button(win_delete, text='Удалить задачу', command=delete_task).pack(side='bottom')
    value.pack(side='bottom')
    area.pack(side='top')
    win_delete.mainloop()

# Создание топ меню
m = Menu(root)
root.config(menu=m)
fm = Menu(m)
m.add_cascade(label="Fie", menu=fm)
fm.add_command(label="Delete task", command=m_delete_task)
fm.add_command(label="Exit", command=root.destroy)
hm = Menu(m)
m.add_cascade(label="Help", menu=hm)
hm.add_command(label="Help")
hm.add_command(label="About")
# Получение даты этого и следующего дня
date = datetime.today()
today = '{0}.{1}.{2}'.format(date.year, date.month, date.day )
tommorow = '{0}.{1}.{2}'.format(date.year, date.month, date.day + 1)
# Проверка на задачи
def task_today(today, root):
    try:
        i = 1
        with open('tasks\\{}.txt'.format(today), encoding='UTF-8') as f:
            f_read = f.readlines()
            for line in f_read:
                task = str(i) + '. ' + line
                i = int(i) + 1
                lab = Label(root, font='Airal 12', bg='white', text=task)
                lab.pack()
        new_task(today, width, height)
    except FileNotFoundError:
        lab = Label(root, font='Airal 14', text='Задач на сегодня нет\n\n')
        lab.pack()
        new_task(today, width, height)
# Новая задача
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
                with open('tasks\\{}.txt'.format(tommorow), 'a', encoding='UTF-8') as f:
                    f.write(task)
            except FileNotFoundError:
                os.mkdir('tasks')
                with open('tasks\\{}.txt'.format(tommorow), 'a', encoding='UTF-8') as f:
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