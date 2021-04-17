from tkinter import *
from tkinter import messagebox
from intermedio.Pilas import pila
from intermedio.notacion import inversa
from intermedio.codigop import CodigoP
class Polaca:
    def __init__(self, lista_cadenas, cadenas):
        self.x = pila()
        #cadena = 'X = 23.3 + 4 - 22 * abc * num4 + 474 - 3 * b'
        
        self.ventana = Toplevel()
        self.ventana.title('Código intermedio')
        self.ventana.geometry('700x400+550+200')
        #print(self.elimina('[43]'))
        self.text = Text(self.ventana)
        self.text.pack()
        print("------",lista_cadenas)
        for i, cadena in enumerate(cadenas):
            self.examinar = self.x.proceso(lista_cadenas[i])
            self.desarrollo(self.examinar,cadena)
            self.text.insert(END, '\n\n')
            self.agrega_inversa(lista_cadenas[i].copy())
            self.text.insert(END, '\n\n')
            self.agregar_codigop(lista_cadenas[i])
            self.text.insert(END, '\n\n\n\n')
        #self.ventana.mainloop()
    def agregar_codigop(self, array):
        self.text.insert(END, "Código P.\n")
        codp = CodigoP().obtener_codigop(array)
        print(array,codp)
        for i in codp:
            self.text.insert(END, i + "\n")
    def agrega_inversa(self, array):
        self.text.insert(END,"Notación Polaca\n")
        array = inversa().obtener_notacion(array)
        print(array)
        list_cads = []
        for paso in array:
            pilas = [[],[]]
            l_opnds = len(paso[0])
            l_opers = len(paso[1])
            cads = []
            if(l_opnds >= l_opers):
                for i in reversed(range(l_opnds)):
                    cad_oper = ""
                    cad_opnd = paso[0][i]
                    if(i < l_opers):cad_oper = paso[1][i]
                    cads.append("%s\t\t%s\n"%(cad_opnd, cad_oper))
            else:
                for i in reversed(range(l_opers)):
                    cad_oper = paso[1][i]
                    cad_opnd = ""
                    if(i < l_opnds):cad_opnd = paso[0][i]
                    cads.append("%s\t\t%s\n"%(cad_opnd, cad_oper))
            list_cads.append((cads, paso[2]))
            print(cads, paso[2])
        list_cads = [i for i in list_cads if len(i[0]) > 0]
        for lineas in list_cads:
            self.text.insert(END,"Operandos\tOperadores\n")
            for linea in lineas[0]:
                self.text.insert(END, linea)
            self.text.insert(END, "\nACC " + lineas[1]+"\n\n\n")
    def desarrollo(self,array,cadena):
        self.text.insert(END, 'Expresion: '+cadena+"\n")
        self.text.insert(END,  'Orden: '+str(" ".join(array))+"\n\n")
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

        self.text.insert(END, "Dirección \t  Operador \t  Operando1 \t  Operando2\n")
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
            if(i == len(self.orden)-1):
                l[0] = l[2]
                l[3] = '---'
                if(len(self.orden) == 1):
                    l[2] = array[2]
                else:
                    l[2] = self.orden[i-1][0]
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

#c = Polaca('X = 23.3 + 4 - 22 * abc * num4 + 474 - 3 * b')


