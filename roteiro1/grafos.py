
class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'


    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not(self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A
        self.Matriz=[]

    def arestaValida(self, aresta=''):
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
        print("teste",aresta)
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0



    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        if self.verticeValido(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not(i == len(self.A) - 1): # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str

    def criamatriz(self):
        '''Função respsonsavel por criar uma matriz para grafos simples, de acordo com a quantidade de vertices
        criados pelo usuario, e contida na variavel do grafo self.Matriz..
        exemplo ['-', '0', '0']
                ['-', '-', '0']
                ['-', '-', '-']
        Como o grafo é simples, a parte da diagonal central para baixo da matriz é completada com caractéres '-', e da 
        diagonal pra cima, é completada por 0, sendo subistituido quando tiver uma aresta na posição.
        '''
        tam = len(self.N)
        matriz = self.Matriz
        for i in range(tam):
            linha = []
            for j in range(tam):
                linha.append('0')
            matriz.append(linha)
        for i in range(tam - 1, -1, -1):
            for j in range(i, -1, -1):
                matriz[i][j] = '-'
        self.Matriz= matriz

    def imprimir(self):
        ''' 
        Função resposnsável por imprimir a matriz.. qualquer hora, qualquer momento só basta chamar...
        '''
        for i in self.Matriz:
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
        v=self.N
        matriz=self.Matriz
        pares = a.values()
        for i in pares:
            elemento = i.split("-")
            tam1 = v.index(elemento[0])
            tam2 = v.index(elemento[1])
            if (tam1 < tam2):
                matriz[tam1][tam2] = '1'
            else:
                matriz[tam2][tam1] = '1'

    def parNaoAdjacente(self):
        '''
        Função coorespondente a questão 3 letra a..
        Retorna os pares de vertices nao adjacentes existentes na matriz...
        '''
        matriz=self.Matriz
        v=self.N
        tam = len(v)
        for i in range(tam):
            for j in range(tam):
                if matriz[i][j] == '0':
                    print(v[i] + "-" + v[j])

