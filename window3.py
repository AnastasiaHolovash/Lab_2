from tkinter import *
import random
from window2 import W2


class W3:
    global A, B, G_A, G_B
    def __init__(self):
        self.men = ['Андрій', 'Антон', 'Денис', 'Богдан', 'Віталій', 'Віктор', 'Костя', 'Сергій', 'Вова']
        self.women = ['Настя', 'Маша', 'Аня', 'Катя', 'Юля', 'Даша', 'Оля', 'Люда']

        self.root = None

    def window3(self):
        global A, B, men, women
        self.slave3 = Toplevel(self.root)
        self.slave3.title('Window3')
        self.slave3.focus_set()

        def A_cholovik_B():
            a = set()
            for i in self.A:
                if i in self.men:
                    a.add(i)
            b = set()
            for j in self.B:
                if j in self.women:
                    b.add(j)
            S = []
            for i in range(min(len(a), len(b))):
                p = random.choice(list(a))
                q = random.choice(list(b))
                S.append([p, q])
                a.remove(p)
                b.remove(q)
            return S

        def A_onuk_B():
            a = set()
            for i in self.A:
                if i in self.men:
                    a.add(i)
            b = self.B
            R = []
            for i in range(min(len(a), len(b))):
                p = random.choice(list(a))
                q = random.choice(list(b))
                if [p, q] not in self.S:
                    if [p, q] not in R:
                        R.append([p, q])
            return R

        self.S = A_cholovik_B()
        self.R = A_onuk_B()

        lf1 = LabelFrame(self.slave3, text='A', font='Arial 12')
        lf1.grid(row=0, column=0)
        listbox1 = Listbox(lf1, font='Arial 14')
        listbox1.grid(row=0, column=0)
        for i in self.A:
            listbox1.insert(END, i)

        scr1 = Scrollbar(lf1, command=listbox1.yview)
        listbox1.configure(yscrollcommand=scr1.set)
        scr1.grid(row=0, column=1, sticky=W, ipady=90)

        lf2 = LabelFrame(self.slave3, text='B', font='Arial 12')
        lf2.grid(row=0, column=2)
        listbox2 = Listbox(lf2, font='Arial 14')
        listbox2.grid(row=0, column=2)
        for j in self.B:
            listbox2.insert(END, j)

        scr2 = Scrollbar(lf2, command=listbox2.yview)
        listbox2.configure(yscrollcommand=scr2.set)
        scr2.grid(row=0, column=3, sticky=W, ipady=90)

        canvS = Canvas(self.slave3, width=600, height=200)
        dict_SA = {}
        dict_SB = {}
        canvS.create_text(160, 30, text='Множина aSb, якщо a чоловік b', font='Arial 16')
        for i in range(len(self.A)):
            canvS.create_text(30 + i * 50, 50, text=list(self.A)[i], font='Arial 10')
            canvS.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
            dict_SA.update({list(self.A)[i]: [30 + i * 50, 80]})
        for j in range(len(self.B)):
            canvS.create_text(30 + j * 50, 190, text=list(self.B)[j], font='Arial 10')
            canvS.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="blue")
            dict_SB.update({list(self.B)[j]: [30 + j * 50, 160]})
        for k in self.S:
            canvS.create_line(dict_SA[k[0]], dict_SB[k[1]], arrow=LAST)
        canvS.grid(row=2, column=0, columnspan=3)

        canvR = Canvas(self.slave3, width=600, height=200)
        dict_RA = {}
        dict_RB = {}
        canvR.create_text(160, 30, text='Множина aRb, якщо a онук b', font='Arial 16')
        for i in range(len(self.A)):
            canvR.create_text(30 + i * 50, 50, text=list(self.A)[i], font='Arial 10')
            canvR.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
            dict_RA.update({list(self.A)[i]: [30 + i * 50, 80]})
        for j in range(len(self.B)):
            canvR.create_text(30 + j * 50, 190, text=list(self.B)[j], font='Arial 10')
            canvR.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="blue")
            dict_RB.update({list(self.B)[j]: [30 + j * 50, 160]})
        for k in self.R:
            canvR.create_line(dict_RA[k[0]], dict_RB[k[1]], arrow=LAST)
        canvR.grid(row=3, column=0, columnspan=3)
