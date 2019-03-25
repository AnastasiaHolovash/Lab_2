from tkinter import *
import pickle


class W2:

    def __init__(self):
        self.B = set()
        self.A = set()
        self.men = ['Андрій', 'Антон', 'Денис', 'Богдан', 'Віталій', 'Віктор', 'Костя', 'Сергій', 'Вова']
        self.women = ['Настя', 'Маша', 'Аня', 'Катя', 'Юля', 'Даша', 'Оля', 'Люда']
        self.root = None

    def window2(self):
        global A, B, G_A, G_B
        G_A = self.A
        G_B = self.B
        print(self.A)
        self.slave2 = Toplevel(self.root)
        self.slave2.title('Window2')
        self.slave2.focus_set()

        def add_to_list_women(event):
            if var.get() == 0:
                self.A.add(self.women[event.widget.curselection()[0]])
            if var.get() == 1:
                self.B.add(self.women[event.widget.curselection()[0]])
            lb['text'] = 'A = {}\nB = {}\n'.format(self.A, self.B)

        def add_to_list_men(event):
            if var.get() == 0:
                self.A.add(self.men[event.widget.curselection()[0]])
            if var.get() == 1:
                self.B.add(self.men[event.widget.curselection()[0]])
            lb['text'] = 'A = {}\nB = {}\n'.format(self.A, self.B)

        def clean_lists():
            self.A = set()
            self.B = set()
            lb['text'] = 'A = {}\nB = {}\n'.format(self.A, self.B)

        def save_to_file():
            self.f = open('МножиниАВ.txt', 'wb')
            pickle.dump(self.A, self.f)
            pickle.dump(self.B, self.f)
            self.f.close()
            but['text'] = 'Збережено'
            but['state'] = DISABLED

        def show_from_file():
            self.show = Toplevel(self.slave2)
            self.show.title('Window2/Show_sets')
            self.show.focus_set()
            self.show.minsize(300, 100)
            self.f = open('МножиниАВ.txt', 'rb')
            Label(self.show, text='A={}\n'
                                  'B={}'.format(pickle.load(self.f), pickle.load(self.f)), font='Arial 14',
                  justify=LEFT) \
                .pack(fill=BOTH)
            self.f.close()

        Label(self.slave2, text='Задайте множини А та В', font='Arial 16 bold').grid(row=0, column=0, columnspan=4)

        var = IntVar()
        var.set(0)
        rad0 = Radiobutton(self.slave2, text="Множина A", font='Arial 12 bold', variable=var, value=0)
        rad1 = Radiobutton(self.slave2, text="Множина B", font='Arial 12 bold', variable=var, value=1)
        rad0.grid(column=0, row=1, sticky=W)
        rad1.grid(column=0, row=2, sticky=W)

        lf1 = LabelFrame(self.slave2, text="Жіночі імена", font='Arial 12')
        lf1.grid(row=3, column=0, columnspan=2)

        listbox1 = Listbox(lf1, selectmode=EXTENDED, font='Arial 14')
        for i in self.women:
            listbox1.insert(END, i)
        listbox1.bind("<<ListboxSelect>>", add_to_list_women)
        listbox1.grid(row=3, column=0)

        scr1 = Scrollbar(lf1, command=listbox1.yview)
        listbox1.configure(yscrollcommand=scr1.set)
        scr1.grid(row=3, column=1, sticky=W, ipady=90)

        lf2 = LabelFrame(self.slave2, text="Чоловічі імена", font='Arial 12')
        lf2.grid(row=3, column=2, columnspan=2)

        listbox2 = Listbox(lf2, selectmode=EXTENDED, font='Arial 14')
        for i in self.men:
            listbox2.insert(END, i)
        listbox2.bind("<<ListboxSelect>>", add_to_list_men)
        listbox2.grid(row=3, column=2)

        scr2 = Scrollbar(lf2, command=listbox2.yview)
        listbox2.configure(yscrollcommand=scr2.set)
        scr2.grid(row=3, column=3, sticky=W, ipady=90)

        Button(self.slave2, text='Очистити множини', font='Arial 12', command=clean_lists) \
            .grid(row=4, column=0, columnspan=2)

        but = Button(self.slave2, text='Зберегти в файл', font='Arial 12', command=save_to_file)
        but.grid(row=4, column=2, columnspan=2)

        Button(self.slave2, text='Показати з файлу', font='Arial 12', command=show_from_file) \
            .grid(row=5, column=2, columnspan=2)

        lf3 = LabelFrame(self.slave2, text='Задані множини', font='Arial 12', )
        lf3.grid(row=6, column=0, columnspan=5, sticky=W)
        lb = Label(lf3, text='A = {}\n'
                             'B = {}\n'.format(self.A, self.B), font='Arial 14', justify=LEFT)
        lb.grid(row=6, column=0, columnspan=5, sticky=W)


