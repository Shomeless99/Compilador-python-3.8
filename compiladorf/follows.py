from preproceso import *
def calcular_follows(firsts, t, gramatica):
    #solo vacios
    followsC = []
    follows = {}
    guardar_recorrido = []
    for i in gramatica:
        key_t = obtener_key(i, 0)
        izq, produce = recorrer_objeto(i)
        guardar_recorrido.append([izq, produce])
        if(len(produce) == 1):
            if(produce[0] == '$'):
                followsC.append(izq)
    if(len(followsC) > 0):
        follows_imp = ''
        
        #print("follows a calcular",followsC)
        acumulado = {}
        for i in followsC:
            acumulado[i] = []
            cont = 0
            ffx = []
            ftx = []
            calculados = 0
            followsCal = [i]
            rep = False
            while(calculados != len(followsCal) or not rep):
                calculados = len(followsCal)
                fnt, ft, ff = calcular_follow(followsCal[cont], guardar_recorrido, t)
                followsCalAnt = followsCal.copy()
                if(len(fnt) > 0):
                    for ix in fnt:
                        e = False
                        for dx in ff:
                            if(dx == followsCal[cont]):
                                e = True
                        

                        if(ix not in followsCal):
                            if(e):followsCal = followsCal[:cont+1]+ [ix] +followsCal[cont+1:]
                            else:followsCal.append(ix)

                            #followsCal.append(ix)
                            #IBASOLO
                if(len(ft) > 0):
                    for ix in ft:
                        if(ix not in ftx):
                            ftx.append(ix)
                if(len(ff) > 0):
                    for ix in ff:
                        if(ix not in ffx):
                            ffx.append(ix)
                #print("ANALIZADO",followsCal[cont])
                sop = []
                for xsi in fnt:
                    if(xsi not in followsCalAnt and xsi not in sop):
                        sop.append(xsi)
                #print(i, sop,ft,ff)

                acumulado[i].append({'fnt':sop,'ft':ft,'ff':ff})
                cont += 1
                if(cont == len(followsCal)):
                    cont = 0
                    rep = True
                
            #print("")
                #FALTA GUARDAR EL FOLLOW (FT) Y AÑADIR LOS FIRSTS
            follows[i] = ftx
            ffx += fnt
            for ix in ffx:
                for jx in firsts[ix]['t']:
                    if(jx not in follows[i]):
                        follows[i].append(jx)
        follimp = ''
        #print(acumulado)
        acumulado_c = {}
       
        fnt_acumulados = []
        for i in followsC:
            follimp += 'Follows(%s) '%(i)
            ac = []
            ult = False
            for j in acumulado[i]:
                follimp += " = "
                ult = False
                ac += j['ft']
                add_ant = False 
                if(len(ac) > 0):
                    follimp += '{'
                    for l in ac:
                        follimp += '%s,'%(l)
                    follimp = follimp[:len(follimp)-1]
                    follimp += '} '
                    add_ant = True
                add_ant2 = False
                if(len(j['ff']) > 0):
                    if(add_ant):
                        follimp += ' + '
                        add_ant = False
                    for k in j['ff']:
                        follimp += 'Firsts(%s) + '%(k)
                        ac += firsts[k]['t']
                    follimp = follimp[:len(follimp)-2]
                    ult = True
                    add_ant2 = True
                fnt_acumulados = j['fnt'] + fnt_acumulados
                #print("FNTAC",fnt_acumulados)
                if(len(fnt_acumulados) > 0):
                    #print("ADDINGFNTAC",fnt_acumulados)
                    ult = True
                    if(add_ant2 or add_ant):
                        follimp += ' + '
                    ap = []
                    for k in fnt_acumulados:
                        if(k not in ap):
                            follimp += 'Follows(%s) + '%(k)
                            ap.append(k)
                    follimp = follimp[:len(follimp)-2]
                fnt_acumulados = fnt_acumulados[1:]
            if(ult):
                follimp += ' = {'
                for l in ac:
                    follimp += '%s,'%(l)
                follimp = follimp[:len(follimp)-1]
                follimp += '} '
            follimp+="\n{}".format(acumulado[i])
            follimp += "\n\n"
        #print(follimp)
    return follows, follimp
def calcular_follow(busq, recorrido, t):
    followsT = []
    followsNT = []
    followsF = []
    for i, rec in enumerate(recorrido):
        for j, key  in enumerate(rec[1]):
            if(key == busq):
                if(j + 1 == len(rec[1])):
                    if(rec[0] == busq):
                        if(busq not in followsF):
                            followsF.append(busq)
                    else:
                        followsNT.append(rec[0])
                else:
                    siguiente_valor = rec[1][j+1]
                    if(siguiente_valor in t):
                        if(siguiente_valor not in followsT):
                            followsT.append(siguiente_valor)
                    else:
                        if(siguiente_valor not in followsNT):
                            followsNT.append(siguiente_valor)
    return followsNT, followsT, followsF