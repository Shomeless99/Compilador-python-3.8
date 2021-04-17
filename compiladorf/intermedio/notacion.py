#!/usr/bin/env python

# -- coding: utf-8 --
from intermedio.Pilas import pila
class inversa():
    def obtener_notacion(self, cadena):
        self.pila_acciones = []
        operadores = ['(', ')', "=", '*', '/', '+', '-',"**"]
        x = ['(','X','=','(','(','(','(','27','/','2',')',')','/','4',')','+','5',')',')']
        x = ["("]+x+[")"]
        x = ['(', 'A', '=', '(','(' ,'(' , '(' ,'98', '/', '4', ')','*', '5', ')', '+', '22',')', '-','5',')',')']
        #x = x[3:len(x)-1]
        x=["(","Y","=","(","12","+","(","5","*","(","3","**","2",")",")",")",")"]
        
        pil = pila()
        x = pil.proceso_lista(cadena)
        #if(x[2] != "("):
        #    x = x[:2] + ["("] + x[2:] + [")"]
        x = ["("]+x+[")"]

        stacknum=[]
        stackope=[]
        print("X", x)
        cad = x
        print("Cadena", cad)
        t=len(cad)
        nota = ""
        elementos_por = []
        conteo = 0
        parentesis = []
        for i in range(t):
            if(cad[i] == ")"):elementos_por.append((i, parentesis.pop()))
            elif(cad[i] not in operadores):
                print(cad[i])
                parentesis[len(parentesis)-1] += 1
            elif(cad[i] == "("):parentesis.append(0)
        print(elementos_por)

        for i in range(t):
            self.pila_acciones.append([stacknum.copy(), stackope.copy(), nota])
            if  cad[i] in operadores:
                if cad[i] == ")":
                    self.pila_acciones[len(self.pila_acciones)-1][1].append(")")
                    n = ["", ""]
                    cant = self.elementos_parentesis(elementos_por, i)
                    for number in range(cant):
                        n[number] += stacknum.pop()
                    if(cant == 0):
                        op = stackope.pop()
                        nota += " %s"%(op)
                        stackope.pop()
                        continue
                    op = stackope.pop()
                    if(op == "("):op = ""
                    elif(len(stackope) > 0):stackope.pop()
                    nota += " %s %s %s"%(n[0], n[1], op)
                    self.pila_acciones[len(self.pila_acciones)-1][2] = nota
                else:stackope.append(cad[i])
            else:stacknum.append(cad[i])
            
        print(nota)
        return self.pila_acciones
    def elementos_parentesis(self, elementos_por, pos):
        for elemento in elementos_por:
            if(elemento[0] == pos):return elemento[1]
    
"""
i=invera()
nota = i.obtener_notacion(["A","=","3","*","10","+","32","*","b"])
nota = i.obtener_notacion(["A","=","3","*","5"])
print(nota)
"""