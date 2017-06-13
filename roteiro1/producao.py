#v=['v','c','r','o','a']
#a={'a1':'v-c','a2':'v-r','a3':'v-o','a5':'c-r','a6':'c-o','a8':'r-o'}

v=['1','2','3','4']
a={'a1':'1-2','a2':'2-3','a3':'3-1'}
a2={'a1':'1-2','a2':'2-4','a3':'4-3','a4':'3-1'}

a3={'a1':'3-2','a2':'2-4','a3':'4-3'}

#v4=['1','2','3','4','5','6','7','8']
#a4={'a1':'1-4','a2':'1-2','a 3':'2-7','a4':'2-5','a5':'5-7','a6':'5-6','a7':'3-6','a8':'3-5'}
v4=['1','2','3','4']
a4={'a1':'1-2','a2':'1-4','a3':'1-3','a4':'3-4'}




def criamatriz(v):
    tam=len(v)
    matriz=[]
    for i in range(tam):
        linha=[]
        for j in range(tam):
            linha.append('0')
        matriz.append(linha)

    for i in range(tam-1,-1,-1):
        for j in range(i,-1,-1):
            matriz[i][j]='-'
    return matriz


def imprimir(matriz):
    for i in matriz:
        print(i)

def criararestaMatriz(matriz,a,v):
    pares=a.values()
    for i in pares:
        elemento=i.split("-")
        tam1=v.index(elemento[0])
        tam2=v.index(elemento[1])
        if(tam1<tam2):
            matriz[tam1][tam2]='1'
        else:
            matriz[tam2][tam1] ='1'

def parNaoAdjacente(matriz,v):
    tam=len(v)
    for i in range(tam):
        for j in range(tam):
            if matriz[i][j]=='0':
                print(v[i]+"-"+v[j])

def grauVertice(matriz,v,vertice):
    pos=v.index(vertice)
    tam=len(v)
    cont=0
    for i in range(tam):
        if(matriz[i][pos]=='1'):
            cont+=1
        if (matriz[pos][i] == '1'):
            cont += 1
    return cont


def arestaNoCuDoVertice(matriz,v,a,vertice):
    pos=v.index(vertice)

    tam = len(v)
    cont = 0
    valores=[]
    chaves=[]

    for i in a.keys():
        chaves.append(i)
    for i in a.values():
        valores.append(i)
    print(chaves)
    print(valores)


    for i in range(tam):
        aux = v[i] + "-" + vertice

        if (matriz[i][pos] == '1'):

            if aux in valores:
                print(chaves[valores.index(aux)])
            else:
                print(chaves[valores.index(aux[::-1])])
        if (matriz[pos][i] == '1'):
            if aux in valores:
                print(chaves[valores.index(aux)])
            else:
                print(chaves[valores.index(aux[::-1])])

def confereGrafoCompleto(matriz,v):

    for j in (v):

        pos=v.index(j)
        tam=len(v)
        cont=0
        for i in range(tam):
            if(matriz[i][pos]=='1'):
                cont+=1
            if (matriz[pos][i] == '1'):
                cont += 1
        if cont<(tam-1):
            return "nao é completo"

    return "é completo"


def confereGrafoConexo(matriz,v):

    for j in (v):
        pos=v.index(j)
        tam=len(v)
        cont=0
        for i in range(tam):
            if(matriz[i][pos]=='1'):
                cont+=1
            if (matriz[pos][i] == '1'):
                cont += 1
        if cont<1:
            return "nao é conexo"

    return "é conexo"
'''
def confereCiclo(matriz, v):
    incial =""
    num = 0
    for j in (v):
        pos = v.index(j)
        tam = len(v)
        anterior = ""
        incial = v[pos]
        print(j)
        cont = 0
        for i in range(tam):
            if(matriz[i][pos]=='1' and v[pos]!= anterior):
                anterior= v[pos]
                cont+=1
            if (matriz[pos][i] == '1'and v[pos]!=anterior):
                anterior = v[pos]
                cont+=1
            print(anterior)
    if v[num]==incial and cont>0:
        return "tem"
'''

def verificaCiclo(matriz,vertice,aresta):
    tam=len(vertice)
    #print(vertice)
    par1=[]
    par2=[]
    ciclos=[]
    for i in range(tam):
        n=[]
        ciclos.append(n)
        for j in range(tam):
            if matriz[i][j] == '1':
                par1.append(i)
                par2.append(j)
    print(par1)
    print(par2)

    foras=[]

    passou=[]
    while True:
         cont=0
         for j in range(len(par1)):

            if (grauVertice(matriz, vertice, vertice[par2[j]]) == 1):
                print("vwertice ", vertice[par2[par1[j]]])
                print("grau ",grauVertice(matriz, vertice, vertice[par2[j]]))
                foras.append(j)
                cont+=1
                continue
            print(par1[j],par2[j])

         indices=[]
         for i in range(len(par2)):
             if not i in foras:
                indices.append(i)
         print("")
         achou=False

         for i in range(len(par1)):
             if achou==True:
                 break
             print(i)
             davez=par2[i]
             possivelciclo=[]
             possivelciclo.append(i)

             while True:
                 if(davez in par1):

                     pos=par1.index(davez)
                     if par1[pos] in possivelciclo and par1[pos] == possivelciclo[0]:
                         if(len(possivelciclo)>2):
                            print("True")
                            print(possivelciclo)
                            achou=True
                            break
                         else:
                             break

                     else:
                        if not davez in possivelciclo and not par1[pos] == possivelciclo[0]:
                            if par1.count(davez)>1:
                                for i in range(len(par1)):
                                    if(par1[i]==davez) and not i ==pos:
                                        pos=i
                                        break
                            #break
                        possivelciclo.append(par1[pos])
                        davez=par2[pos]
                 else:
                     pos = par2.index(davez)
                     if par2[pos] in possivelciclo and par2[pos] == possivelciclo[0]:
                         if(len(possivelciclo)>2):
                            print("True")
                            print(possivelciclo)
                            achou=True
                            break
                         else:
                             break
                     else:
                         if not davez in possivelciclo and not par2[pos] == possivelciclo[0]:
                             if par2.count(davez) > 1:
                                 for i in range(len(par2)):
                                     if (par2[i] == davez) and not i == pos:
                                         pos = i
                                         break

                         possivelciclo.append(par2[pos])
                         davez = par1[pos]
                 if len(possivelciclo)>len(par1):
                     break

         break
    if achou==False:
        print("False")





m=criamatriz(v)
#imprimir(m)
criararestaMatriz(m,a,v)

#parNaoAdjacente(m,v)
#print(v)

print()
#print(grauVertice(m,v,'o'))

#arestaNoCuDoVertice(m,v,a,'o')
#print(confereGrafoConexo(m,v))
#print(confereCiclo(m, v))

'''

m2=criamatriz(v)
imprimir(m)
print()
criararestaMatriz(m2,a2,v)
print(a2)
imprimir(m2)

print()

m3=criamatriz(v)
criararestaMatriz(m3,a3,v)
print(a3)
imprimir(m3)


print()
'''
m4=criamatriz(v4)
print(a4)
criararestaMatriz(m4,a4 ,v4)
imprimir(m4)
print("\n")
verificaCiclo(m4,v4,a4)
#print(grauVertice(m4,v4,"4"))