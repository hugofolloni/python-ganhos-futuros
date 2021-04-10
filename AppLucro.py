from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonttxt = ('Calibri', '10', 'bold')
        self.fontctn = ('Calibri', '8')

        self.primeirocontainer = Frame(master)
        self.primeirocontainer['padx'] = 40
        self.primeirocontainer['pady'] = 20
        self.primeirocontainer.pack()

        self.segundocontainer = Frame(master)
        self.segundocontainer['padx'] = 40
        self.segundocontainer['pady'] = 5
        self.segundocontainer.pack()

        self.terceirocontainer = Frame(master)
        self.terceirocontainer['padx'] = 40
        self.terceirocontainer['pady'] = 5
        self.terceirocontainer.pack()

        self.quartocontainer = Frame(master)
        self.quartocontainer['padx'] = 20
        self.quartocontainer['pady'] = 60

        self.titulo = Label(self.primeirocontainer, text="Ajudante de Investimentos")
        self.titulo['font'] = ('Calibri', '15', 'bold')
        self.titulo.pack()

        ativo = StringVar()

        self.lblativo = Label(self.segundocontainer, text='Seu ativo:')
        self.lblativo['font'] = self.fonttxt
        self.lblativo.pack(side=LEFT)

        self.entryativo = Entry(self.segundocontainer, textvariable = ativo)
        self.entryativo['width'] = 15
        self.entryativo['font'] = self.fontctn
        self.entryativo.pack(side=LEFT)

        self.btnativo = Button(self.segundocontainer, text="Confirmar!", font=self.fontctn, width=10, command=self.funcA)
        self.btnativo.pack(side=RIGHT)

        self.rsptativo = Label(self.terceirocontainer, text='')
        self.rsptativo.pack()

    def funcA(self):
        self.btnativo['command'] = self.confativo()
        self.btnativo['command'] = self.aparecer()

    def confativo(self):
        ativo = self.entryativo.get()
        print(ativo)
        self.rsptativo.config(text='Vamos estudar sobre o ativo {}!'.format(ativo))

    def aparecer(self):
        master = None
        self.ctntempo = Frame(master)
        self.ctntempo['padx'] = 20
        self.ctntempo['pady'] = 5
        self.ctntempo.pack()

        self.ctnvarano = Frame(master)
        self.ctnvarano['padx'] = 20
        self.ctnvarano['pady'] = 5
        self.ctnvarano.pack()

        self.ctndivy = Frame(master)
        self.ctndivy['padx'] = 20
        self.ctndivy['pady'] = 5
        self.ctndivy.pack()

        self.ctninvest = Frame(master)
        self.ctninvest['padx'] = 20
        self.ctninvest['pady'] = 5
        self.ctninvest.pack()

        self.ctnbtn = Frame(master)
        self.ctnbtn['padx'] = 20
        self.ctnbtn['pady'] = 10
        self.ctnbtn.pack()

        self.ctnresult = Frame(master)
        self.ctnresult['padx'] = 40
        self.ctnresult['pady'] = 30
        self.ctnresult.pack()

        self.ctntotal = Frame(master)
        self.ctntotal['padx'] = 20
        self.ctntotal['pady'] = 5
        self.ctntotal.pack()


        self.lbltempo = Label(self.ctntempo, text='Anos de investimento:', font=self.fonttxt, width=40)
        self.lbltempo.pack(side=LEFT)

        self.t = float()
        self.divy = float()
        self.invest = float()
        self.varano = float()

        self.enttempo = Entry(self.ctntempo, textvariable='t')
        self.enttempo['width'] = 10
        self.enttempo['font'] = self.fontctn
        self.enttempo.pack()

        self.lblvarano = Label(self.ctnvarano, text='Variação anual média do preço do ativo:', font=self.fonttxt,
                               width=40)
        self.lblvarano.pack(side=LEFT)

        self.entvarano = Entry(self.ctnvarano, textvariable='varano', width=10, font=self.fontctn)
        self.entvarano.pack()

        self.lbldivy = Label(self.ctndivy, text='Dividend Yield médio: ', font=self.fonttxt, width=40)
        self.lbldivy.pack(side=LEFT)

        self.entdivy = Entry(self.ctndivy, textvariable='divy', width=10, font=self.fontctn)
        self.entdivy.pack()

        self.lblinvest = Label(self.ctninvest, text='Quanto já investiu no ativo:', width=40, font=self.fonttxt)
        self.lblinvest.pack(side=LEFT)

        self.entinvest = Entry(self.ctninvest, textvariable='invest', width=10, font=self.fontctn)
        self.entinvest.pack()

        self.btnresult = Button(self.ctnbtn, text='Resultado', command=self.verResultado, width=10, font=self.fonttxt)
        self.btnresult.pack()

        self.lblresult = Label(self.ctnresult, text='')
        self.lblresult.pack()

        self.lbltotal = Label(self.ctnresult, text='', font=('Verdana', '10', 'bold'))
        self.lbltotal.pack()

    def verResultado(self):

        self.t = float(self.enttempo.get())
        self.varano = float(self.entvarano.get())
        self.divy = float(self.entdivy.get())
        self.invest = float(self.entinvest.get())

        self.totalvar = self.invest * ((1 + (self.varano / 100)) ** self.t)
        self.totaldivy = self.invest * self.divy / 100 * self.t
        self.total = self.totaldivy + self.totalvar + self.invest

        self.t = float(self.t)
        self.totalvar = float(self.totalvar)
        self.totaldivy = float(self.totaldivy)
        self.total = float(self.total)

        self.lblresult.config(text="Seu investimento renderá, dentro de {:.0f} anos, {:.2f} reais em valorização e {:.2f} reais em dividendos".format(self.t, self.totalvar, self.totaldivy))
        self.lbltotal.config(text='O total será de {:.2f} reais!'.format(self.total))

root = Tk()
Application(root)
root.mainloop()
