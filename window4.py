from tkinter import *
import copy


class W4:
    def __init__(self):
        self.root = None

    def window4(self):
        global A, B
        self.slave4 = Toplevel(self.root)
        self.slave4.title('Window4')
        self.slave4.focus_set()
        self.slave4.minsize(700, 300)
        self.slave4.maxsize(700, 300)

        def but1():
            canv.delete("all")
            canv.create_text(150, 20, text='R \u222A S', font='Arial 16')
            dict_b1 = {}
            dict_b2 = {}
            V = self.R + self.S
            for i in range(len(self.A)):
                canv.create_text(30 + i * 50, 50, text=list(self.A)[i], font='Arial 10')
                canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
                dict_b1.update({list(self.A)[i]: [30 + i * 50, 80]})
            for j in range(len(self.B)):
                canv.create_text(30 + j * 50, 190, text=list(self.B)[j], font='Arial 10')
                canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="blue")
                dict_b2.update({list(self.B)[j]: [30 + j * 50, 160]})
            for k in V:
                canv.create_line(dict_b1[k[0]], dict_b2[k[1]], arrow=LAST)

        def but2():
            canv.delete("all")
            canv.create_text(150, 20, text='R \u2229 S', font='Arial 16')
            dict_b1 = {}
            dict_b2 = {}
            V = []
            for i in self.R:
                if i in self.S:
                    V.append(i)

            for i in range(len(self.A)):
                canv.create_text(30 + i * 50, 50, text=list(self.A)[i], font='Arial 10')
                canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
                dict_b1.update({list(self.A)[i]: [30 + i * 50, 80]})
            for j in range(len(self.B)):
                canv.create_text(30 + j * 50, 190, text=list(self.B)[j], font='Arial 10')
                canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="blue")
                dict_b2.update({list(self.B)[j]: [30 + j * 50, 160]})

            for k in V:
                if len(V) != 0:
                    canv.create_line(dict_b1[k[0]], dict_b2[k[1]], arrow=LAST)

        def but3():
            canv.delete("all")
            canv.create_text(150, 20, text='R \ S', font='Arial 16')
            dict_b1 = {}
            dict_b2 = {}
            V = copy.deepcopy(self.R)
            for i in V:
                if i in self.S:
                    V.remove(i)

            for i in range(len(self.A)):
                canv.create_text(30 + i * 50, 50, text=list(self.A)[i], font='Arial 10')
                canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
                dict_b1.update({list(self.A)[i]: [30 + i * 50, 80]})
            for j in range(len(self.B)):
                canv.create_text(30 + j * 50, 190, text=list(self.B)[j], font='Arial 10')
                canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="blue")
                dict_b2.update({list(self.B)[j]: [30 + j * 50, 160]})
            for k in V:
                canv.create_line(dict_b1[k[0]], dict_b2[k[1]], arrow=LAST)

        def but4():
            canv.delete("all")
            canv.create_text(150, 20, text='U \ R', font='Arial 16')
            dict_b1 = {}
            dict_b2 = {}

            V = []
            a = set()
            for i in self.A:
                if i in self.men:
                    a.add(i)
            b = copy.deepcopy(self.B)
            for i in a:
                for j in b:
                    V.append([i, j])

            for i in V:
                if i in self.R:
                    V.remove(i)

            for i in range(len(self.A)):
                canv.create_text(30 + i * 50, 50, text=list(self.A)[i], font='Arial 10')
                canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
                dict_b1.update({list(self.A)[i]: [30 + i * 50, 80]})
            for j in range(len(self.B)):
                canv.create_text(30 + j * 50, 190, text=list(self.B)[j], font='Arial 10')
                canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="blue")
                dict_b2.update({list(self.B)[j]: [30 + j * 50, 160]})
            for k in V:
                if len(V) != 0:
                    canv.create_line(dict_b1[k[0]], dict_b2[k[1]], arrow=LAST)

        def but5():
            canv.delete("all")
            canv.create_text(150, 20, text='S⁻¹', font='Arial 16')
            dict_b1 = {}
            dict_b2 = {}
            V = copy.deepcopy(self.S)
            for i in V:
                i[0], i[1] = i[1], i[0]
            for i in range(len(self.A)):
                canv.create_text(30 + i * 50, 50, text=list(self.A)[i], font='Arial 10')
                canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="green")
                dict_b1.update({list(self.A)[i]: [30 + i * 50, 80]})
            for j in range(len(self.B)):
                canv.create_text(30 + j * 50, 190, text=list(self.B)[j], font='Arial 10')
                canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="blue")
                dict_b2.update({list(self.B)[j]: [30 + j * 50, 160]})
            for k in V:
                canv.create_line(dict_b2[k[0]], dict_b1[k[1]], arrow=LAST)

        Label(self.slave4, text='   ').grid(row=0, column=0)
        Label(self.slave4, text='Операції над відношеннями', font='Arial 16').grid(row=0, column=2, columnspan=2)
        Button(self.slave4, text='R \u222A S', font='Arial 12', command=but1) \
            .grid(row=1, column=1, sticky=W)
        Button(self.slave4, text='R \u2229 S', font='Arial 12', command=but2) \
            .grid(row=2, column=1, sticky=W)
        Button(self.slave4, text='R \ S', font='Arial 12', command=but3) \
            .grid(row=3, column=1, sticky=W)
        Button(self.slave4, text='U \ R', font='Arial 12', command=but4) \
            .grid(row=4, column=1, sticky=W)
        Button(self.slave4, text='S⁻¹', font='Arial 12', command=but5) \
            .grid(row=5, column=1, sticky=W)
        Label(self.slave4, text='   ').grid(row=0, column=2)

        canv = Canvas(self.slave4, width=600, height=250)
        canv.grid(row=1, column=3, rowspan=6)
