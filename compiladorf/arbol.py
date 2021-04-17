from graphviz import Digraph
from gramatica import gramatica_individual
from preproceso import obtener_terminales, obtener_tipos

def generar_arbol(datos, numero):
    g = Digraph('structs', filename='structs_revisited%i.gv'%(numero),
            node_attr={'shape': 'record'})
    #s.graph_attr.update(rank='min')
    ns = 1
    rank = 0
    ultima_fila = [datos[0][0]]
    nodos_ultima_fila = []
    conexiones = []
    nodos_ultima_fila.append('struct%i'%(ns))
    g.node('struct%i'%(ns),r'{%s}'%(datos[0][0]))
    
    niveles = [[(datos[0][0],'struct%i'%(ns))]]
    terminales, _ = obtener_terminales(gramatica_individual)
    ns = 2
    print(terminales)
    actual_fila = 1
    while(actual_fila < len(datos)):
        fila = datos[actual_fila]
        #if(comienzo > 0):comienzo-=1
        #if(ultima_fila[comienzo] != fila[comienzo]): comienzo -= 1

        
        #print(niveles)
        #print(fila)
        #print(niveles)
        if(niveles == []):
            print(datos)
            print(fila)
            input()
        if(len(fila) == 0):
            print("s",fila)
            actual_fila += 1
        elif(len(fila) >= len(ultima_fila)):
            if(fila != ultima_fila and fila[len(fila)-1] not in terminales):
                niveles.append([[ff,""] for ff in fila[len(ultima_fila)-1:]])
            if(fila[len(fila)-1] in terminales):
                print(niveles)
                if(fila[len(fila)-1] in obtener_tipos(gramatica_individual, niveles[len(niveles)-1][len(niveles[len(niveles)-1])-1][0])):
                    print(fila[len(fila)-1],'terminales')
                    print("filass",datos[actual_fila+1])
                    print(fila)
                    niveles.append([[fila[len(fila)-1],""]])
                    for niv in range(len(niveles)):
                        if(niveles[niv][len(niveles[niv])-1][1] == ""):
                            if(niv > 0):
                                g.node('struct%i'%(ns),r'{%s|valor}'%(niveles[niv][len(niveles[niv])-1][0]))
                                niveles[niv][len(niveles[niv])-1][1] = 'struct%i'%(ns)
                                conexiones.append((niveles[niv-1][len(niveles[niv-1])-1][1], 'struct%i'%(ns)))
                                ns += 1
                            print("cr")
                    niveles[len(niveles)-1].pop()
                    actual_fila += 1  
                else:
                    try:
                        if(niveles[len(niveles)-1] == []):
                            niveles = niveles[:len(niveles)-1]
                        niveles[len(niveles)-1].pop()
                        if(niveles[len(niveles)-1] == []):
                            niveles.pop()
                    except:pass  
            else:
                
                actual_fila += 1
        else:
            try:
                if(niveles[len(niveles)-1] == []):
                    niveles = niveles[:len(niveles)-1]
                niveles[len(niveles)-1].pop()
                if(niveles[len(niveles)-1] == []):
                    niveles.pop()
            except:pass
        ultima_fila = fila
    #g.graph_attr["rankdir"] = "TB"
    #g.graph_attr.update(rank='min')
    g.edges(conexiones)
    g.view()

def obtener_datos(raw_datos, numero):
    for fila in raw_datos:
        pass
    datos = raw_datos
    generar_arbol(datos)
        

