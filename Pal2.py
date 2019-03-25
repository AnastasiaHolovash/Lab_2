from tkinter import *
import window2
import window3
import window4


win2 = window2.W2()
win3 = window3.W3()
win4 = window4.W4()


class Lab2:
    A = set()
    B = set()

    def student(self, n=3, g=64):
        self.slave = Toplevel(self.root)
        self.slave.title('Student')
        self.slave.focus_set()
        self.slave.minsize(300, 100)
        self.slave.maxsize(300, 100)
        self.slave.wm_geometry("+600+250")
        Label(self.slave, text='Бровченко Анастасія\n'
                               'група ІО-64\n'
                               'варіант {}'.format((n + g % 60) % 30 + 1),
              justify=LEFT, font="Arial 17 bold").pack(fill='both')

    def mainwindow(self):
        self.root = Tk()
        self.root.title('Window1')
        self.root.minsize(500, 200)
        self.root.maxsize(500, 200)
        self.root.wm_geometry("+500+200")

        Label(self.root, text='Лабораторна робота №2\n'
                              '«Бінарні відношення та їх основні властивості,\n'
                              ' операції над відношеннями»\n', font="Arial 16 bold").grid(row=0, column=0, columnspan=4)
        Button(self.root, text='Window2', font="Arial 12", command=win2.window2).grid(row=1, column=0)
        Button(self.root, text='Window3', font="Arial 12", command=win3.window3).grid(row=2, column=0)
        Button(self.root, text='Window4', font="Arial 12", command=win4.window4).grid(row=3, column=0)

        Button(self.root, text='Студент', font='Arial 14', height=2, width=10,
               command=self.student).grid(column=2, row=1, sticky=E, rowspan=2)
        self.root.mainloop()


Nastya = Lab2()
Nastya.mainwindow()
