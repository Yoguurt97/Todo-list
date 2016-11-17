import os
from datetime import datetime
from tkinter import *
from ctypes  import *

# TODO Один файл в неделю/месяц
# TODO Доработка GUI

class buttons():
    def tmr_tasks(self):
        root = Tk()
        root.geometry('500x300+{0}+{1}'.format(int(width), int(height)))
        root.title('Задачи на завтра')
        try:
            with open('tasks\\{}.txt'.format(tommorow), encoding='UTF-8') as f:
                pass
        except FileNotFoundError:
            root.geometry('100x40+{0}+{1}'.format(int(width), int(height)))
            btn = Button(root, text='Задач на завтра нет', command=root.destroy).place(x=3)
        root.mainloop()
    def about(self):
        root = Tk()
        root.title('About')
        root.geometry('600x400+{0}+{1}'.format(int(width), int(height)))
        with open('LICENSE.txt', 'r') as f:
            lic = f.read()
            Label(root, text=lic).pack()
        root.mainloop()
    def new_task(self):
        pass
    def delete_tasks(self):
        win_delete = Tk()
        win_delete.geometry('300x120+{0}+{1}'.format(int(width), int(height)))
        area = Label(win_delete, text='Введите дату задачи, \nкоторые хотите удалить(ГГГГ.ММ.Д)\n')
        value = Entry(win_delete)
        def delete_task():
            try:
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

# Проверка на задачи
def task_today(today, root):
    try:
        i = 1
        with open('tasks\\{}.txt'.format(today), encoding='UTF-8') as f:
            lab = Label(root, font='Airal 14', bg='white', text='\n\nЗадачи на сегодня: \n')
            lab.pack()
            f_read = f.readlines()
            for line in f_read:
                task = str(i) + '. ' + line
                i = int(i) + 1
                lab = Label(root, font='Airal 12', bg='white', text=task)
                lab.pack()
            tmr_btn = Button(root, text='Задачи на завтра', command=buttons.tmr_tasks).place(y=250, x=190)
        new_task(today, width, height)
    except FileNotFoundError:
        lab = Label(root, font='Airal 14', bg='white', text='Задач на сегодня нет\n\n')
        lab.place(y=50, x=150)
        tmr_btn = Button(root, text='Задачи на завтра', command=buttons.tmr_tasks).place(y=90, x=190)
        new_task(today, width, height)
# Новая задача
def new_task(today, width, height):
    text_task = Entry(root, width=54, font='Arial 14')
    text_task.place(x=0)
    def add_task():
        task = text_task.get()
        if task == '':
            error_win = Tk()
            error_win.geometry('100x100+{0}+{1}'.format(int(width), int(height)))
            error_win.title('Ошибка')
            error = Label(error_win, text='Задача\n не может быть пустой')
            ok_added = Button(error_win, text='Оk', command=error_win.destroy)
            text_task.delete('0', END)
            ok_added.pack()
            error.pack()
            error_win.mainloop()
        else:
            try:
                with open('tasks\\{}.txt'.format(tommorow), 'a', encoding='UTF-8') as f:
                    f.write(task + '\n')
            except FileNotFoundError:
                os.mkdir('tasks')
                with open('tasks\\{}.txt'.format(tommorow), 'a', encoding='UTF-8') as f:
                    f.write(task + '\n')
            task_add = Tk()
            task_add.geometry('100x100+{0}+{1}'.format(int(width), int(height)))
            task_add.title('Ok')
            added = Label(task_add, text='Задача добавлена')
            ok_added = Button(task_add, text='Оk', command=task_add.destroy)
            text_task.delete('0', END)
            ok_added.pack()
            added.pack()
            task_add.mainloop()
    btn = Button(root, text='Добавить задачу', command=add_task)
    btn.place(x=400)
    root.mainloop()

if __name__ == '__main__':
    buttons = buttons()
    # Получение даты этого и следующего дня
    date = datetime.today()
    today = '{0}.{1}.{2}'.format(date.year, date.month, date.day)
    tommorow = '{0}.{1}.{2}'.format(date.year, date.month, date.day + 1)
    # Получение разешения экрана пользователя
    width = windll.user32.GetSystemMetrics(0) / 4 - 50
    height = windll.user32.GetSystemMetrics(1) / 4 - 50
    # Создание окна
    root = Tk()
    root.resizable(width=False, height=False)
    root.geometry('500x300+{0}+{1}'.format(int(width), int(height)))
    root.title('Todo list')
    root['bg'] = 'white'
    # Создание топ меню
    m = Menu(root)
    root.config(menu=m)
    fm = Menu(m)
    m.add_cascade(label="Fie", menu=fm)
    fm.add_command(label="New task", command=buttons.new_task)
    fm.add_command(label="Delete task", command=buttons.delete_tasks)
    fm.add_command(label="Exit", command=root.destroy)
    hm = Menu(m)
    m.add_cascade(label="Help", menu=hm)
    hm.add_command(label="About", command=buttons.about)
    task_today(today, root)
    root.mainloop()