import datetime
import os
from tkinter import *
from ctypes  import *

# TODO Один файл в неделю/месяц
# TODO Доработка GUI, сделать более приятный дизайн, добавить оповещение о добавленной задачи, убрать {} в задачах на сегодня.

width = windll.user32.GetSystemMetrics(0) / 4 - 50
height = windll.user32.GetSystemMetrics(1) / 4 - 50
width = int(width)
height = int(height)

root = Tk()
root.geometry('700x500+{0}+{1}'.format(width, height))
root.title('Todo list')
root['bg'] = 'white'


list_tasks = []

date = datetime.datetime.today()
today = str(date.year) + '.' + str(date.month) + '.' + str(date.day)
next_day = date.day + 1
tommorow = str(date.year) + '.' + str(date.month) + '.' + str(next_day)


def task_today(today, list_tasks, root):
    i = 1
    try:
        with open('tasks\\' + today + '.txt', 'r', encoding='UTF-8') as f:
            f_read = f.readlines()
            print('Задачи на сегодня ' + today + ':')
            for line in f_read:
                i = str(i)
                print(i + '. ' + line)
                task = i + '. ' + line
                list_tasks.append(task)
                i = int(i)
                i += 1
                lab = Label(root, font='Airal 12', bg='white', text=task)
                lab.pack()
        new_task(today, width, height)
    except FileNotFoundError:
        lab = Label(root, font='Airal 14', text='Задач на сегодня нет\n\n')
        lab.pack()
        print('Задач на сегодня нет\n\n')
        new_task(today, width, height)

def new_task(today, width, height):
    text_task = Text(root, height=7, width=300, font='Arial 14', wrap=WORD)
    text_task.pack()
    def add_task():
        task = text_task.get('1.0', END)
        try:
            with open('tasks\\' + tommorow + '.txt', 'a', encoding='UTF-8') as f:
                f.write(task)
        except FileNotFoundError:
            os.mkdir('tasks')
            with open('tasks\\' + tommorow + '.txt', 'a', encoding='UTF-8') as f:
                f.write(task)
        task_add = Tk()
        task_add.geometry('100x100+{0}+{1}'.format(width, height))
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

task_today(today, list_tasks, root)
root.mainloop()