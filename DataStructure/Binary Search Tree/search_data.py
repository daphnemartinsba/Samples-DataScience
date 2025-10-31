class no:
    def __init__(self, valor):
        self.chave = valor
        self.fe = None
        self.fd = None

def buscar(raiz, valor): # a função utiliza o valor da raiz e o valor do elemento a ser buscado
    no_atual = raiz
    while no_atual != None and no_atual.chave != valor: # Pergunta se o nó atual (no primeiro laço a raiz) é diferente de nulo e se sua chave (valor da raiz no primeiro laço) é diferente do valor procurado, se for igual à raiz, ele encontrou o que buscava e retorna o valor da raiz. Caso o valor procurado seja menor que o valor da raiz, no primeiro laço, o nó atual deixará de ter o valor da raiz e passará a ter o valor do filho esquerdo da raiz, no_atual = fd (o mesmo procedimento ocorre se for maior, com o filho direito). O laço perguntará novamente, se o valor for igual ao valor chave do no_atual (agora fe da raiz), o algoritmo encontrou e retorna o fe da raiz. Caso não, e o valor seja novamente menor que o nó atual, o no atual passa a ser o fe do no_atual(fe da raiz) e assim sucessivamente, até encontrar ou até o fim.
        if valor < no_atual.chave: 
            no_atual = no_atual.fe
        else:
            no_atual = no_atual.fd
    return no_atual # por conta da variável raiz.fe da linha 16, o valor retornado (encontrado) é 5, do fe

raiz = no(7)
raiz.fe = no (5)
no = buscar(raiz, 5)
