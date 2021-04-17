#!/usr/bin/env python
# -- coding: utf-8 --

class CodigoP():
    def __init__(self):

        self.acciones = []
        #self.recolecta()
        #self.inicia()
        #self.combina()
        #print("STO")
        
        self.acciones.append("STO")
        print(self.acciones)
    def obtener_codigop(self, cadena):
        self.acciones = []
        self.recolecta(cadena[2:])
        self.inicia(cadena[0])
        self.combina()
        self.acciones.append("STO")
        print(self.acciones)
        return self.acciones
    def recolecta(self, cadena):
        x = "";
        for i in cadena:
            x+=i
        print("X",x)
        cad=(str(x))# se hace cadena para hacer el recorrido
        print("Cadena",cad)
        tam=len(cad)
        print("T", tam)
        c=0
        c2=0
        self.L=[]
        self.L2=[]
        car=""
        for i in range(tam):
            if cad[i]=='*' or cad[i]=='/' or cad[i]=='+' or cad[i]=='-':
                c+=1
                self.L.append(car)
                car=""
                self.L2.append((cad[i]))
            else:
                c2+=1
                car+=cad[i]
        if(car!=""):self.L.append(car)
        print ("signos encontrados",c)
        print("numeros encontrados encontrados", c2)
        print("numeros encontrados",self.L)
        print("Signos encontrados",self.L2)

    def inicia(self, first):
        X = first#Variable a utlizar para iniciar el proceso, esta cambia deacuerdo a lo mandado
        print("LDA", X)
        self.acciones.append("LDA %s"%(X))
        x = len(self.L)
        self.xx = 0
        self.primeros = []
        for i in range(x):
            if i == 0 or i == 1:
                try:
                    self.xx = int(self.L[i])
                    self.acciones.append("LDC %s"%(self.xx))
                except:
                    try:
                        self.xx = float(self.L[i])
                        self.acciones.append("LDC %s"%(self.xx))
                    except:
                        self.xx = self.L[i]
                        self.acciones.append("LOD %s"%(self.xx))
                        
                self.primeros.append(self.L[i])
                print("LDC", self.xx)
                

    def combina(self):
        ss = len(self.L)
        ss2 = len(self.L2)
        s = ss + ss2
        c = 0
        c1 = 0
        c2 = 2
        x = ''
        x2 = 0
        #uno=self.primeros[0]
        #dos=self.primeros[1]
        while c <= s:
            if c == 0 or c % 2 == 0:
                if(c1 == len(self.L2)):break
                x = self.L2[c1]
                if x == '*':
                    print("MPI")
                    self.acciones.append("MPI")
                elif x == '/':
                    print("DIV")
                    self.acciones.append("DIV")
                elif x == '+':
                    print("ADI")
                    self.acciones.append("ADI")
                elif x == '-':
                    print("SBI")
                    self.acciones.append("SBI")
                x=''
                c1 += 1
                c += 1
            elif c % 2 != 0:
                if(c2 == len(self.L)):break
                try:
                    x2 = int(self.L[c2])
                    self.acciones.append("LDC %s"%(x2))
                except:
                    try:
                        x2 = float(self.L[c2])
                        self.acciones.append("LDC %s"%(x2))
                    except:    
                        x2 = self.L[c2]
                        self.acciones.append("LOD %s"%(x2))

                c2 += 1
                print("LDC", x2)
                
                #print("C2",c2)
                c+=1

"""
codp=CodigoP()
codp.obtener_codigop(["A", "=","b"])
codp.obtener_codigop(["A","=","B","*","30"])
"""