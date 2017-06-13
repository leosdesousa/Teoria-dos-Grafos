from grafos import Grafo


'''
Testando a classe Grafo.... 

N = {J, C, E, P, M, T, Z}
A = {a1, a2, a3, a4, a5, a6, a7, a8, a9}
g(a1) = JC, g(a2) = CE, g(a3) = CE, g(a4) = CP, g(a5) = CP, g(a6) = CM, g(a7) = CT, g(a8) = MT, g(a9) = TZ


g=Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],{'a1':'J-C', 'a2':'C-E',
		'a3':'C-E','a4':'C-P', 'a5':'C-P', 'a6':'C-M','a7':'C-T',
		'a8':'M-T', 'a9':'T-Z'})
		
print(g)


'''
#implementando..

def arestaValida(V=[], aresta=''):
	'''
    Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
    Uma aresta é representada por um string com o formato a-b, onde:
    a é um substring de aresta que é o nome de um vértice adjacente à aresta.
    - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
    b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
    Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
    :param aresta: A aresta que se quer verificar se está no formato correto.
    :return: Um valor booleano que indica se a aresta está no formato correto.
    '''

	# Não pode haver mais de um caractere separador
	if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
		return 1  #erro de separador

	# Índice do elemento separador
	i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

	# O caractere separador não pode ser o primeiro ou o último caractere da aresta
	if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
		return 2 #codigo do traco

	if not aresta[:i_traco] in V or not aresta[i_traco + 1:] in V:
		return 3 #codigo aresta nao contem dentro dos vertices

	return 0 #nao aconteceu erro..

def verificaListaVertice(vertices=''):
	'''
    Verifica uma lista de vértices passados por parâmetro está dentro do padrão estabelecido.
    Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
    :param vertice: Um string que representa o vértice a ser analisado.
    :return: Um valor booleano que indica se o vértice está no formato correto.
    '''

	v = vertices.split(", ")
	flag = False
	SEPARADOR_ARESTA2 = ['-', '(', ')', ' ']  # E, R, T, ,R

	while True:
		if flag==True:
			v1=input("Erro: Digite novamente")
			v = v1.split(", ")
			flag=False

		for vertice in v:
			for testes in SEPARADOR_ARESTA2:
				if (testes in vertice or (vertice == '')):
					flag = True

		if flag==False:
			break
	return v


def ConverteListaDicionario(V=[],aresta=''):
	'''Recebe uma string do tipo aresta realiza os teste '''
	dici = {}
	erro = False

	while True:
		if erro == True:
			aresta = input("Digite novamente as arestas: ")
			dici = {}
			erro =False

		dicionario_parcial = aresta.split(", ")
		for dp in dicionario_parcial:
			if dp.count('(') == 1 and dp.count(')') == 1:
				aux = dp.split("(")
				retorno_erro=arestaValida(V,aux[1][:-1])
				if (retorno_erro != 0):
					if retorno_erro==1:
						print("Verifique os Separadores das arestas.. ")
					elif(retorno_erro==2):
						print("Pocisao do caractere sepadador.. ")
					elif(retorno_erro==3):
						print("Aresta contem vertices invalidos  ",aux[1][:-1],"vertices validos",v)
					erro=True
				dici[aux[0]] = aux[1][:-1]
				aux=''
			else:
				print("Erro de chaves..  ")
				erro=True
		if erro == False:
			break



	return dici


def VerificaParNaoAdjacente(Grafo):
	for par in Grafo.N:
		for aux in Grafo.N:
			if not(Grafo.existeAresta(''+par+'-'+aux+'')):
				if not(Grafo.existeAresta(''+aux+'-'+par+'')):
					print(par+"-"+aux,Grafo.existeAresta(''+par+'-'+aux+''))


#vertices = input(" Digite os vertives separados por , e um espaco: ")
#v=verificaListaVertice(vertices)
v=verificaListaVertice("J, C, E, A")
#dici = input("Digite as arestas :")

#a = ConverteListaDicionario(dici)
a=ConverteListaDicionario(v,"a3(J-C), a4(C-E), a5(A-E)")
g=Grafo(v,a)
print(g)
g.criamatriz()
g.imprimir()
print()
g.criararestaMatriz()
g.imprimir()
g.parNaoAdjacente()

#VerificaParNaoAdjacente(g)







