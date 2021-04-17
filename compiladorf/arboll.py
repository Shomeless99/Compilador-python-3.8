from graphviz import Digraph
from preproceso import obtener_terminales,obtener_tipos
from gramatica import gramatica_individual




def generar_arbol(datos, numero):
    terminales,_ = obtener_terminales(gramatica_individual)
    nuevos_datos = []
    des = False
    last_long = 0
    for i in range(len(datos)):
        if(datos[i] in [[],'']):
            last_long = len(datos[i])
            continue
        if(i > 0):
            if(len(datos[i]) < last_long):
                des = True
                
                print("here",len(datos[i]), last_long)
                last_long = len(datos[i])
            else:des = False
        if(des and i+1<len(datos)):
            if(datos[i-1][len(datos[i-1])-1] in terminales and len(datos[i+1]) < len(datos[i])):
                el = nuevos_datos.pop()
                print("eliminando",el)
            else:print("terminal",nuevos_datos[len(nuevos_datos)-1])
        nuevos_datos.append(datos[i])
        last_long = len(datos[i])
    for i in nuevos_datos:
        print(i)
    #datos = nuevos_datos
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
    ns = 2
    niveles = []
    terminales,_ = obtener_terminales(gramatica_individual)
    for fila in datos[1:]:
        if(len(fila) >= len(ultima_fila)):
            comienzo = len(ultima_fila)
            #if(comienzo > 0):comienzo-=1
            #if(ultima_fila[comienzo] != fila[comienzo]): comienzo -= 1
            try:
                nodo = nodos_ultima_fila.pop()
                print(nodo)
                niveles.append(fila)
                for ij in range(comienzo-1,len(fila)):
                    print(terminales)
                    if(fila[ij] in terminales):
                        #if(fila[ij] in)
                        print("TIPOS")
                        print(fila[ij],ultima_fila[len(ultima_fila)-1])
                        print(obtener_tipos(gramatica_individual, ultima_fila[len(ultima_fila)-1]))
                        
                        if(fila[ij] not in obtener_tipos(gramatica_individual, ultima_fila[len(ultima_fila)-1])):
                            ultima_fila = fila
                            nodos_ultima_fila.append('struct%i'%(ns-1))
                            continue
                        g.node('struct%i'%(ns),r'{%s}'%(fila[ij]))
                    else:
                        g.node('struct%i'%(ns),r'{%s|valor}'%(fila[ij]))
                    print("declaracion nodo",'struct%i'%(ns),fila[ij])
                    conexiones.append((nodo, 'struct%i'%(ns)))
                    nodos_ultima_fila.append('struct%i'%(ns))
                    ns += 1
                rank += 1
            except:pass
        else:
            try:
                nodos_ultima_fila.pop()
            except:pass
        print(nodos_ultima_fila)
        ultima_fila = fila
    #g.graph_attr["rankdir"] = "TB"
    #g.graph_attr.update(rank='min')
    g.edges(conexiones)
    g.view()

def obtener_datos(raw_datos):
    for fila in raw_datos:
        pass
    datos = raw_datos
    generar_arbol(datos)
        

