class no:
    def __init__(self, valor):
        self.chave = valor
        self.fe = None
        self.fd = None

def buscar(raiz, valor): # a função utiliza o valor da raiz e o valor do elemento a ser buscado
    no_anc = None # Começa como vazio, pois começará a possuir valor quando o laço começar depois de validar que o valor não é igual a none nem raiz
    no_atual = raiz
    while no_atual != None and no_atual.chave != valor: # se encontrar o valor ou none, o laço acaba
        no_anc = no_atual # na primeira volta, o ancestral é a raiz, se o valor for menor que ela, o ancestral passará a ser o fe
        if valor < no_atual.chave: 
            no_atual = no_atual.fe
        else:
            no_atual = no_atual.fd
    return no_atual, no_anc # Retorna o valor encontrado, ou none no caso de não achar o valor procurado e retorna o valor do nó ancestral (o último nó percorrido antes de encontrar o elemento ou none)

def conectar(anc, no): # essa função é chamada pela função inserir() 
    if no.chave < anc.chave: # compara valor do novo nó com a chave
        anc.fe = no
    elif no.chave > anc.chave:
        anc.fd = no

def inserir(raiz, no, valor):
    novo = no(valor) #cria um novo no com o valor que deve ser inserido
    if raiz == None:
        raiz = novo # caso seja uma árvore vazia, insere o valor como raiz
    else:
        no, anc = buscar(raiz, valor) # se a árvore tiver raiz, a função de busca vai retornar o valor caso ele exista na árvore, ou vai retornar um espaço vazio. Também retorna seu ancestral, pela variável anc (pós virgula), essa informação vai ser utilizada pela função conectar para ligar o novo nó à um ancestral
        conectar(anc,novo) # a conectar função pega o nó ancestral retornado pela busca e pega o novo nó, na variável novo
        print('No('+str(anc.chave)+')') # imprime nó ancestral como string
        
raiz = no(7)
nova = 5
funcao = inserir(raiz, no, nova)


# Explicação da função buscar():
# Para inserir é primeiro necessário fazer uma busca, 
# contudo, a busca, além de reconhecer a raiz, como no_atual no ponto de partida do laço 
# deve reconhecer os seus filhos como nós ancestrais, quando estes passarem como no_atual no laço 
# isto é, quando a busca não encontra o elemento na raiz, 
# ela compara se o valor é menor ou maior que a chave (valor) da raiz 
# dependendo da comparação, se o valor é menor que a raiz, 
# Na volta do laço o valor comparado com o (valor) do filho esquerdo 
# e NESTE MOMENTO o filho esquerdo da raiz se torna o nó ancestral 
# porque caso o valor seja diferente dele (fe, vulgo nó ancestral)
# o valor será comparado a ele, se menor, na próxima volta do laço será comparado com seu fe
# e assim, sucessivamente, até encontrar o elemento, ou retornar vazio. 
# No caso da inserção é interessante que retorne vazio
