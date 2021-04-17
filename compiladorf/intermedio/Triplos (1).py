from tkinter import *
from tkinter import messagebox
from Pilas import pila

class Polaca:

    def __init__(self):
        self.x = pila()
        cadena = 'X = 12 * 3 + 5 * 5 / 3'
        #cadena = 'X = 10 * 3 * 4 + 43 * 54 + 13 - 11'
        cadena = 'C = 4 + b + 12 * 5 - 2 + 5 * 6 * 7'
        self.examinar = self.x.proceso(cadena)
        print('Expresion Final: '+str(self.examinar))
        self.ventana = Tk()
        self.ventana.title('Triplos')
        self.ventana.geometry('700x400+550+200')
        #print(self.elimina('[43]'))
        self.desarrollo(self.examinar,cadena)
        self.ventana.mainloop()
    def desarrollo(self,array,cadena):
        self.l = Label(text='Expresion: '+cadena)
        self.l.pack()
        self.l2 = Label(text = 'Orden: '+str(" ".join(array)))
        self.l2.pack()
        self.text = Text(self.ventana)
        self.text.pack()
        self.text.insert(END,'Triplos: \n')
        self.orden = []
        self.c = 0
        self.valor = 0
        band = True
        while band != False:
            if(len(array) <= 3):
                lista = []
                lista.append('['+str(self.valor)+']')
                lista.append(array[1])
                lista.append(array[0])
                lista.append(array[2])
                self.orden.append(lista)
                band = False
            else:
                pos = 0
                pos2 = 0
                for i in range(len(array)):
                    if(array[i] == '('):
                        pos = i
                    if(array[i] == ')'):
                        pos2 = i
                        break
                lista = []
                lista.append('['+str(self.valor)+']')
                lista.append(array[pos+2])
                lista.append(array[pos+1])
                lista.append(array[pos+3])


                array.pop(pos)
                array.pop(pos)
                array.pop(pos)
                array.pop(pos)
                array.pop(pos)

                array.insert(pos,'['+str(self.valor)+']')
                self.orden.append(lista)
                self.valor+=1
                print(array)

        print(self.orden)

        self.text.insert(END, "Descripcion \t  Operador \t  Operando1 \t  Operando2\n")
        for i in range(len(self.orden)):
            self.l = self.orden[i]
            for b in range(len(self.l)):
                self.text.insert(END,str(self.l[b])+'\t\t')
            self.text.insert(END,'\n')


        self.text.insert(END,'\n \n')
        self.text.insert(END, 'Cuadruplos: \n')
        self.text.insert(END, 'Operador \t  Operando1 \t  Operando2  \t\t Auxiliar\n')
        for i in range(len(self.orden)):
            ll = self.orden[i]
            for i in range(len(ll)):
                x = list(ll[i])
                if x[0] == '[':
                    b = self.elimina(str(ll[i]))
                    ll[i] = "V"+str(int(b)+1)
        for i in range(len(self.orden)):
            l = self.orden[i]
            self.text.insert(END, str(l[1])+'\t\t')
            self.text.insert(END, str(l[2]) + '\t\t')
            self.text.insert(END, str(l[3]) + '\t\t')
            #x = self.elimina(str(l[0]))
            #c = "V"+str(int(x)+1)
            self.text.insert(END, str(l[0]) + '\n')

    def elimina(self,var):
        lista = list(var)
        print(lista)
        c = ''
        for i in range(len(lista)):
            if not (lista[i] == '[' or  lista[i] == ']'):
                c+=lista[i]
        return c

c = Polaca()


