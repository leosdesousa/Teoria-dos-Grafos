
class Grafo:
    def __init__(self,Vertice=[],aresta={}):
        self.matriz=None;
        self.V=Vertice
        self.A=aresta

    def criamatriz(self):
        '''Função que é responsavel por criar uma matriz de acordo com os vertices informados
            retorna: sefine a matriz criada em selv.matriz
        '''
        v=self.V
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
        self.matriz= matriz

    def imprimir(self):
        '''
        Função resposnsável por imprimir a matriz.. qualquer hora, qualquer momento só basta chamar...
        '''
        matriz=self.matriz
        print("\n")
        for i in matriz:
            print(i)

    def criararestaMatriz(self):
        '''
            Função que posiciona as ligações das arestas na matriz, quando houver.
            E faz esse pocisionamento substituindo os '0' por '1' e assim indicando que nessa posição existe uma aresta
            conectando os vertices correspondetes a coordenada.

            exemplo:
            ['-', '0', '0']
            ['-', '-', '0']
            ['-', '-', '-']

            arestas C-E, J-C
            ['-', '1', '0']
            ['-', '-', '1']
            ['-', '-', '-']
            '''
        a=self.A
        v=self.V
        matriz=self.matriz
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

    def grauVertice(self,vertice):
        matriz=self.matriz
        v=self.V
        pos=v.index(vertice)
        tam=len(v)
        cont=0
        for i in range(tam):
            if(matriz[i][pos]=='1'):
                cont+=1
            if (matriz[pos][i] == '1'):
                cont += 1
        return cont

    def arestaNoCuDoVertice(self,vertice):
        matriz=self.matriz
        v=self.V
        a=self.A
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

    def confereGrafoCompleto(self):
        matriz=self.matriz
        v=self.V

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

    def confereGrafoConexo(self,v):
        matriz=self.matriz

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

    def ciclo(self):
        matriz=self.matriz
        aresta=self.A
        vertice=self.V
        tam = len(vertice)
        # print(vertice)
        par1 = []
        par2 = []
        ciclos = []
        for i in range(tam):
            n = []
            ciclos.append(n)
            for j in range(tam):
                if matriz[i][j] == '1':
                    par1.append(i)
                    par2.append(j)

        saida=False

        for i in range(len(vertice)):
            lista_ciclo = []
            visitados=[]
            x=i
            if(self.grauVertice(str(x))==1):
                continue
            lista_ciclo.append(x)
            flag=False
            cont = 0
            while True:
                if cont==len(vertice):
                    break
                cont+=1

               # print(encontrapar(x,par1,par2))
                aux=self.encontrapar(x, par1, par2,visitados,matriz,vertice)
                if len(aux)>=1:
                    for i in aux:
                        x=i
                        if( self.grauVertice(str(i)) > 1):
                            if not i in lista_ciclo:
                                lista_ciclo.append(i)
                                x=i
                                break
                            else:
                                if len(lista_ciclo)>2:
                                    if lista_ciclo[0] in aux:
                                        for j in aux:
                                            if lista_ciclo[0]==j and not aux[j] ==x:

                                                #lista_ciclo.append(aux[j])
                                                if j==lista_ciclo[0]:
                                                    print("Ciclo ", lista_ciclo)
                                                    flag=True
                                                    break

                        if flag == True:
                            break

                if flag==True:
                    break
            if flag == True:
                break
        if len(lista_ciclo)<=2:
            print(False)

    def encontrapar(self,vertice,par1,par2,visitados,matriz,ver):
        lista=[]

        for i in range(len(par1)):
            if par1[i] == vertice:
                    lista.append(par2[i])
            else:
                if par2[i] == vertice:
                    lista.append(par1[i])

        return lista

    def encontrapar2(self,vertice,par1,par2,visitados):
        proximo=-1
        vertice=int(vertice)
        flag=False
        for i in range(len(par1)):
            if par1[i] == vertice and visitados[i]==0:
                proximo=par2[i]
                visitados[i]=1
                flag=True
                break

        #se nao tiver na primeia lista ele acaba
        if(flag==False):
            for i in range(len(par2)):
                if par2[i] == vertice and visitados[i]==0:
                        proximo=par1[i]
                        visitados[i]=1
                        break

        return proximo

    def caminhoEuleriano(self):

        matriz=self.matriz
        vertice=self.V
        tam = len(vertice)

        # print(vertice)
        par1 = []
        par2 = []
        ciclos = []
        for i in range(tam):
            n = []
            ciclos.append(n)
            for j in range(tam):
                if matriz[i][j] == '1':
                    par1.append(i)
                    par2.append(j)
        visitados=[0]*len(par1)

        impares=[]
        par=True
        existe=True
        for i in vertice:
            grau=self.grauVertice(i)
            if(grau%2!=0):
                par=False
                impares.append(int(i))

        if(par==True):
            davez=(min(vertice))
        else:
            if(len(impares)!=2):
                existe=False
            else:
                davez=impares[0]

        if(existe==True):
            caminho=[]
            caminho.append(int(davez))
            if(par==True):
                controle=len(vertice)+2
            else:
                controle=len(vertice)+1
            for i in range(controle):
                    davez=self.encontrapar2(davez,par1,par2,visitados)
                    caminho.append(davez)

            if(par==True):
                if(caminho[0]==caminho[-1]):

                    print("Caminho euleriano PAR ",caminho)
                else:
                    print("Ocorreu algum erro")
            else:
                if(caminho[0]==impares[0] and caminho[-1]==impares[1]):
                    print("O caminho euleriano com dois vertices impares é ", caminho)
                else:
                    print("O caminho nao existe")

        else:
            print("Nao existe caminho euleriano")








#exemplo par
v4=['0','1','2','3','4','5']
a4={'a1':'0-1','a2':'0-2','a6':'1-3','a3':'2-3','a4':'1-4','a5':'4-5','a7':'2-5','a8':'1-2'}


g=Grafo(v4,a4)

g.criamatriz()
g.criararestaMatriz()
g.imprimir()
g.caminhoEuleriano()
g.ciclo()
#exemplo impar
v5=['0','1','2','3','4','5']
a5={'a1':'0-1','a2':'0-2','a6':'1-3','a3':'2-3','a4':'1-4','a5':'4-5','e':'2-5'}


g1=Grafo(v5,a5)

g1.criamatriz()
g1.criararestaMatriz()
g1.imprimir()
g1.caminhoEuleriano()
g1.ciclo()




#exemplo que nao existe
v7=['0','1','2','3','4','5']
a7={'a1':'0-1','a2':'0-2','a6':'1-3','a3':'2-3','a4':'1-4','e':'2-5','e2':'3-5'}


g3=Grafo(v7,a7)

g3.criamatriz()
g3.criararestaMatriz()
g3.imprimir()
g3.caminhoEuleriano()
g3.ciclo()


class Warshalll:
    def __init__(self,Vertice=[],aresta={}):
        self.matriz=None;
        self.V=Vertice
        self.A=aresta

    def imprimir(self):
        print("\n")
        for i in self.matriz:
            print(i)

    def criamatrizAdjacente(self):

          '''Função responsavel por criar a matriz, que permite grafos direcionais, onde será usada no
           algoritmo de Warshall, que faz necessário o uso das direções.'''
          v=self.V
          tam=len(v)
          matriz=[]
          for i in range(tam):
              linha=[]
              for j in range(tam):
                  linha.append('0')
              matriz.append(linha)

          self.matriz= matriz

    def criararestaMatrizAdjacente(self):
          '''Função que preenche a matriz de forma direcional, sendo usada
          pelo algoritmo de Warshall, que difere grafos direcionados de não direcionados,
          sendo necessário essa função para seu funcionamento.'''
          a=self.A
          v=self.V
          pares=a.values()
          for i in pares:
              elemento=i.split("-")
              tam1=v.index(elemento[0])
              tam2=v.index(elemento[1])

              self.matriz[tam1][tam2]='1'

    def algoritmoWarshall(self):
          '''Função responsável por encontrar todos os destinos possíveis de um vértice partido dele,
            até os outros através das conexões de cada vértice completando a matriz gerada a partir dos
            vértices e arestas passadas. Retorna a matriz “E” Preenchida. '''
          matriz=self.matriz
          E = []
          for i in range(len(matriz)):
              E.append(matriz[i])


          for i in range(len(E)):
              for j in range(len(E[i])):
                  if E[j][i] == '1':
                      for k in range(len(E)):
                          E[j][k] = max(E[j][k], E[i][k])

          self.matriz=E
print("\nWARSALL\n")
v = ['A', 'B', 'C', 'D', 'E']
a = {'a1': 'B-A', 'a3': 'D-A','a4': 'A-E', 'a5': 'D-B', 'a6': 'C-D','a7': 'C-E'}
warshall=Warshalll(v,a)
warshall.criamatrizAdjacente()
warshall.criararestaMatrizAdjacente()
warshall.algoritmoWarshall()
warshall.imprimir()

