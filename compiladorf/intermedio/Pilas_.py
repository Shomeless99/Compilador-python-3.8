class pila:
    def __init__(self):
        self.n = ['0','1','2','3','4','5','6','7','8','9']
        self.operadores = ['+','*','/','-','**']
        self.letras = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
                       'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    def proceso(self,cadena):
        self.cadena = self.eliminaEspacios(list(cadena))
        #self.cadena2 = self.agrupar(self.cadena)
        print(self.cadena)
        self.cadena2 = self.une(self.cadena)
        print(self.cadena2)
        self.todo = self.jerarquia(self.cadena2)
        return self.todo

    def proceso_lista(self, cadena):
        pro = self.jerarquia(cadena)
        if(len(pro) == 3):pro = pro[:2] + ["("] + pro[2:] + [")"]
        return pro
    def jerarquia(self, array):
        self.expresion2 = array
        #self.prueba = self.MulDiv(self.expresion)
        #self.expresion2 = self.potencias(self.expresion)
        self.expresion3 = self.MulDiv(self.expresion2)
        self.expresion4 = self.SumRes(self.expresion3)
        return self.expresion4

        #c = ''
        #for i in range(len(self.expresion4)):
        #    c+=self.expresion4[i]
        #    c+=" "
        #print(c)

    def SumRes(self,array):
        self.c2 = 0
        self.pos2 = 0
        self.vv2 = len(array)
        while self.pos2 < self.vv2:
            print('Evaluando: '+str(array[self.c]))
            if array[self.pos2] == '-' or array[self.pos2] == '+':
                self.x2 = True
                self.y2 = True
                try:
                    print(int(array[self.pos2 - 1]))
                except:
                    try:
                        print(float(array[self.pos2 - 1]))
                    except:
                        self.x2 = False
                try:
                    print(int(array[self.pos2 + 1]))
                except:
                    try:print(float(array[self.pos2 + 1]))
                    except:
                        self.y2 = False

                zz = list(array[self.pos2-1])
                zz2 = list(array[self.pos2+1])
                if(zz[0] in self.letras):
                    self.x2 = True
                if(zz2[0] in self.letras):
                    self.y2 = True

                self.c2 = self.pos2
                if (self.x2 == True and self.y2 == True):
                    array.insert(self.c2 - 1, '(')
                    print(array)
                    self.vv2 += 1
                    self.c2 += 1
                    array.insert(self.c2 + 2, ')')
                    print(array)
                    self.vv2 += 1
                    self.c2 += 1
                if (self.x2 == False and self.y2 == True):
                    #modificar como el de abajo el while
                    if (self.c2 + 2 > self.vv2):
                        array.insert(self.vv2 - 1, ')')
                    else:
                        array.insert(self.c2 + 2, ')')
                    print(array)
                    self.vv2 += 1
                    v = self.c2
                    band = False
                    c1 = 0
                    c2 = 0
                    pos = 0
                    b = False
                    while v >= 0:
                        # print('Analizando ratrado: '+str(array[v]))
                        if (array[v] == ')' and b == False):
                            c1 += 1
                        if (array[v] == '('):
                            c2 += 1
                        v -= 1
                    print(c2)
                    print(c1)

                    x = 0
                    pp = self.c2
                    while pp >= 0:
                        if array[pp] == '(':
                            x+=1
                            if x == c2:
                                array.insert(pp,'(')
                                break
                        pp-=1
                    self.vv2 += 1
                    self.c2 += 1
                    print(array)

                if (self.x2 == True and self.y2 == False):
                    #print('Entro a numero y parentesis')
                    pos = 0
                    v = self.c2
                    b = False
                    c1 = 0
                    c2 = 0
                    while v < len(array):
                        #print('Analizando ratrado: '+str(array[v]))
                        if (array[v] == '(' and b == False):
                            c1+=1
                        if(array[v] == ')'):
                            b = True
                            c2 +=1
                        if(array[v] == '(' and b == True):
                            break
                        v += 1
                    x = 0
                    for i in range(self.c2,len(array)):
                        if array[i] == ")":
                            x+=1
                            if x == c2:
                                array.insert(i,')')
                                break
                    self.vv2 += 1
                    print(array)
                    array.insert(self.c2 - 1,'(')
                    self.c2 += 1
                    self.vv2 += 1
                if(self.x2 == False and self.y2 == False):
                    #print('Entro al false de los dos lados')
                    #insercion de lado derecho
                    v = self.c2
                    b = False
                    c1 = 0
                    c2 = 0
                    while v < len(array):
                        # print('Analizando ratrado: '+str(array[v]))
                        if (array[v] == '(' and b == False):
                            c1 += 1
                        if (array[v] == ')'):
                            b = True
                            c2 += 1
                        if (array[v] == '(' and b == True):
                            break
                        v += 1
                    x = 0
                    for i in range(self.c2, len(array)):
                        if array[i] == ")":
                            x += 1
                            if x == c2:
                                array.insert(i, ')')
                                break
                    self.vv2 += 1
                    print(array)

                    #Insercion de lado izquierdo
                    vv = self.c2
                    c1 = 0
                    c2 = 0
                    b = False
                    while vv >= 0:
                        # print('Analizando ratrado: '+str(array[v]))
                        if (array[vv] == ')'):
                            c1 += 1
                        if (array[vv] == '('):
                            c2 += 1
                        vv -= 1

                    x = 0
                    pp = self.c2
                    if(c1 == c2):
                        while pp >= 0:
                            if array[pp] == '(':
                                x += 1
                                if x == c2:
                                    array.insert(pp, '(')
                                    break
                            pp -= 1
                        self.vv2 += 1
                        self.c2 += 1
                    print(array)

                else:
                    pass
                    # print('Te la pelaste')
                self.pos2 = self.c2 + 1
            else:
                self.pos2 += 1
        return array

    def MulDiv(self, array):
        self.c = 0
        self.pos = 0
        self.vv = len(array)
        while self.pos < self.vv:
            #print("Analizando: " + str(array[self.pos]))
            if array[self.pos] == '*' or array[self.pos] == '/':
                self.x = True
                self.y = True
                try:
                    print(int(array[self.pos-1]))
                except:
                    try:print(float(array[self.pos-1]))
                    except:self.x = False
                try:
                    print(int(array[self.pos+1]))
                except:
                    try:print(float(array[self.pos+1]))
                    except:self.y = False

                zz = list(array[self.pos - 1])
                zz2 = list(array[self.pos + 1])
                if (zz[0] in self.letras):
                    self.x = True
                if (zz2[0] in self.letras):
                    self.y = True

                self.c = self.pos
                if(self.x == True and self.y == True):
                    array.insert(self.c-1,'(')
                    print(array)
                    self.vv+=1
                    self.c+=1
                    array.insert(self.c+2,')')
                    print(array)
                    self.vv+=1
                    self.c+=1

                if(self.x == False and self.y == True):
                    if (self.c + 2 > self.vv):
                        array.insert(self.vv - 1, ')')
                    else:
                        array.insert(self.c + 2, ')')
                    print(array)
                    self.vv += 1
                    v = self.c
                    band = False
                    c1 = 0
                    c2 = 0
                    pos = 0
                    while v >= 0:
                        # print("Analizando retrado: "+str(array[v]))
                        if array[v] == '(':
                            pos = v
                        v -= 1
                    array.insert(pos, '(')
                    self.vv += 1
                    self.c += 1
                    print(array)

                if(self.x == True and self.y ==  False):
                    pos = 0
                    v = self.c
                    b = False
                    c1 = 0
                    c2 = 0
                    while v < len(array):
                        # print('Analizando ratrado: '+str(array[v]))
                        if (array[v] == '(' and b == False):
                            c1 += 1
                        if (array[v] == ')'):
                            b = True
                            c2 += 1
                        if (array[v] == '(' and b == True):
                            break
                        v += 1
                    x = 0
                    for i in range(self.c, len(array)):
                        if array[i] == ")":
                            x += 1
                            if x == c2:
                                array.insert(i, ')')
                                break
                    self.vv += 1
                    print(array)
                    array.insert(self.c - 1, '(')
                    self.c += 1
                    self.vv += 1
                if (self.x == False and self.y == False):
                    # print('Entro al false de los dos lados')
                    # insercion de lado derecho
                    v = self.c
                    b = False
                    c1 = 0
                    c2 = 0
                    while v < len(array):
                        # print('Analizando ratrado: '+str(array[v]))
                        if (array[v] == '(' and b == False):
                            c1 += 1
                        if (array[v] == ')'):
                            b = True
                            c2 += 1
                        if (array[v] == '(' and b == True):
                            break
                        v += 1
                    x = 0
                    for i in range(self.c, len(array)):
                        if array[i] == ")":
                            x += 1
                            if x == c2:
                                array.insert(i, ')')
                                break
                    self.vv += 1
                    print(array)

                    # Insercion de lado izquierdo
                    vv = self.c
                    c1 = 0
                    c2 = 0
                    b = False
                    while vv >= 0:
                        # print('Analizando ratrado: '+str(array[v]))
                        if (array[vv] == ')' and b == False):
                            c1 += 1
                        if (array[vv] == '('):
                            b = True
                            c2 += 1
                        if ((array[vv] == ')' and b == True) or (array[vv] == '=' and b == True)):
                            break
                        vv -= 1

                    x = 0
                    pp = self.c
                    while pp >= 0:
                        if array[pp] == '(':
                            x += 1
                            if x == c2:
                                array.insert(pp, '(')
                                break
                        pp -= 1
                    self.vv += 1
                    self.c += 1
                    print(array)
                else:
                    pass
                    #print('Te la pelaste')
                self.pos = self.c + 1
            else:
                self.pos += 1
        return array

    def eliminaEspacios(self,array):
        self.array = array
        c = 0
        x = len(self.array)
        while c < x:
            if(self.array[c] == ' '):
                self.array.pop(c)
                if c == 0:
                    x = len(self.array)
                else:
                    x = len(self.array)
            c+=1
        return self.array
    def agrupar(self, array):
        c = ''
        lista = []
        for i in range(len(array)):
            if(array[i] in self.n):
                c+=array[i]
            else:
                if(c == ''):
                    lista.append(array[i])
                else:
                    lista.append(c)
                    lista.append(array[i])
                c = ''
        lista.append(c)
        return lista
    def p(self, array):
        c = ''
        lista = []
        for i in range(len(array)):
            if(array[i] in self.operadores):
                c+=array[i]
            else:
                if(c == ''):
                    lista.append(array[i])
                else:
                    lista.append(c)
                    lista.append(array[i])
                c = ''
        lista.append(c)
        return lista
    def une(self,array):
        lista  = []
        c = True
        lista.append(array[0])
        lista.append(array[1])
        cad = ''
        for i in range(2, len(array)):
            if(array[i] in self.operadores):
                lista.append(cad)
                lista.append(array[i])
                cad = ''
            else:
                cad+=str(array[i])
        lista.append(cad)
        return lista

c = pila()
#c.proceso('c = 45 + 13 * 2 * 3 / 3')
#c.proceso('x = 98 * 3 + 4 + 4 + 6 * 6 + 3 / 8')
print(c.proceso('X = 12 + 5 * 3 * 2'))