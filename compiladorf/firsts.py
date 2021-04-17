from preproceso import *

def obtener_first(gramatica, nt, terminales, first, relacion, puntero):
    ##print(puntero)
    ##print(nt)

    try:
        clave = gramatica[nt][puntero][0]
    except:
        return first,relacion
    if(clave in terminales):
        first.append(clave)
        relacion.append(nt)
        ##print(first)
        ##print(relacion)
        puntero += 1
        try:
            if(puntero == len(gramatica[relacion[len(relacion)-1]])):
                return first,relacion
        except:pass

        x,y = obtener_first(gramatica, nt, terminales, first, relacion, puntero)
        first += x
        relacion += y
        return first,relacion
    else:
        
        x, y = obtener_first(gramatica, gramatica[nt][0][0], terminales, first, relacion, 0)
        return first,relacion
def obtener_first_ind(gramatica, nt, terminales, first, relacion, puntero):
    try:
        clave = gramatica[nt][puntero][0]
        tabla_valor = gramatica[nt][puntero]
    except:
        return nt,nt
    if(clave in terminales):
        return clave, tabla_valor
    else:
        return clave,tabla_valor
def obtener_firsts(gramatica, terminales, no_terminales):
    firsts = {}
    valores = {}
    pendientes = {}
    for i in no_terminales:
        firsts[i] = []
        valores[i] = []
        pendientes[i] = []
        puntero = 0
        conteo = 0
        analizar = gramatica[i].copy()

        while(puntero < len(analizar) and type(analizar[puntero]) == list):
            clave, valor = obtener_first_ind(gramatica, analizar[puntero][0], terminales, [], [], puntero)
            if(clave in terminales):
                
                if(clave not in firsts[i] and clave == analizar[puntero][0]):
                    firsts[i].append(clave)
                    valores[i].append(analizar[puntero])
                    
                        #input()
                puntero += 1
            else:
                if(valor not in analizar and [valor] not in analizar and valor in pendientes[i]):
                    analizar.append(valor)
                if(type(valor)==str):
                    pass
                    #pendientes[i].append([valor])
                else:
                    if(clave == analizar[puntero][0]):
                        pendientes[i].append(valor)
                puntero+=1
            ##print("c",clave)
            ##print("v",valor)
            ##print("a",analizar)
            ##print("p",pendientes)
            ##print("\n\n")
        
        for isx in analizar:
            if(type(isx) == list):
                if(isx[0] in no_terminales and isx not in pendientes[i]):
                    pendientes[i].append(isx)
        
    ##print("FIST",i)
    ##print(firsts)
    ##print(valores)
    ##print(pendientes)

    firsts, valores,fimpresion = calcular_firsts(firsts, valores, pendientes, terminales, no_terminales)
    return convertir_firsts(firsts, valores, no_terminales),fimpresion
def obtener_conteo(objeto):
    conteo = 0
    for i in objeto:
        conteo += i
    return conteo
def calcular_firsts(firsts, valores, pendientes,terminales, no_terminales):
    conteo_pendientes = 1
    hechos = {}
    ##print("\n\npendientesANTIGUO",pendientes)
    for i in no_terminales:
        hechos[i] = []
        added = 0
        for jx, j in enumerate(valores[i]):
            ##print("jo, ",j[0])
            if(j[0] in no_terminales and j not in pendientes[i]):
                pendientes[i].insert(added, j)
                hechos[i].append(1)
                added += 1
        for j in range(added,len(pendientes[i])):
            if(len(pendientes[i]) > 0):
                hechos[i].append(1)
            else:
                hechos[i].append(0)
    ##print("pendientesNUEVO")
    ##print(pendientes)
    ##print("\n\n",hechos)
    ##print(hechos)
    ##print(valores)
    #exit()
    fi = {}
    for xi in no_terminales:
        fi[xi] = []
        cad = '{'
        for xs in firsts[xi]:
            cad = cad + xs + ','
        cad = cad[:len(cad)-1]
        cad += '}'

        cad2 = ''
        for cc, xs in enumerate(pendientes[xi]):
            if(hechos[xi][cc] == 1):
                cad2 += 'Firsts(%s) + '%(xs[0])
        cad2 = cad2[:len(cad2)-2]
        fi[xi].append(cad)
        fi[xi].append(cad2)
        fi[xi].append('\n')

    while(conteo_pendientes != 0):
        conteo_pendientes = 0
        ##print(pendientes)
        for i in no_terminales:
            pendiente = False
            for ix, j in enumerate(pendientes[i]):
                clave = j[0]
                
                if(hechos[i][ix] != 0):
                    if(obtener_conteo(hechos[clave]) == 0 or (i in pendientes[clave][0] and clave in pendientes[i][0] and obtener_conteo(hechos[clave]) == 1)):
                        for ic, elem in enumerate(firsts[clave]):
                            if(elem not in firsts[i]):
                                firsts[i].append(elem)
                                valores[i].append(j)
                        hechos[i][ix] = 0
                    else:
                        conteo_pendientes+=1
            cad = '{'
            for xs in firsts[i]:
                cad = cad + xs + ','
            cad = cad[:len(cad)-1]
            cad += '}'

            cad2 = ''
            for cc, xs in enumerate(pendientes[i]):
                if(hechos[i][cc] == 1):
                    cad2 += 'Firsts(%s) + '%(xs[0])
            cad2 = cad2[:len(cad2)-2]
            fi[i].append(cad)
            fi[i].append(cad2)
            fi[i].append('\n')
    ##print(hechos)

    return firsts, valores, imprimir_firsts(fi, no_terminales)
def imprimir_firsts(firsts, no_terminales):
    fimpresion = ""
    for i in no_terminales:
        ant = '-as-'
        ant2 = '-as-'
        concat = 'Firsts(%s) = '%(i)
        for j in range(len(firsts[i])):
            if(firsts[i][j] == '\n'):
                if(ant != firsts[i][j-2] and ant2 != firsts[i][j-1]):
                    ant = firsts[i][j-2]
                    ant2 = firsts[i][j-1]
                    if(len(ant)>2):
                        concat += ant + ' + ' + ant2 + ' = '
                    else:
                        concat += ant2 + ' = '
        concat = concat[:len(concat)-5]
        fimpresion +=concat+"\n\n"
    return fimpresion
