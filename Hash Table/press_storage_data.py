def criarTabela(M):
    tabela = {}
    for chave in range(M):
        tabela[chave] = None
    return tabela

def quantidadeInsercao(T,K,Q):
    passo = 0
    while passo < Q:
        D = int(input())
        C = D % K
        T[C] = D
        print(D, '->', C)
        passo = passo + 1

def entradaValores():
    Q = input()
    dividir = Q.split()
    valor1 = dividir[0]
    valor2 = dividir[1]
    quantidade = int(valor1)
    M = int(valor2)
    
    T = criarTabela(M)
    quantidadeInsercao(T,M,quantidade)
    
X = entradaValores() # valores de quantidade de chaves e tamanho da tabela vem juntos como uma string


# Uma função de dispersão h deve transformar uma chave x em um endereço-base h(x) da tabela de dispersão. 
# A finalidade da função de dispersão é produzir um número baixo de colisões entre as chaves. 
# O método da divisão é um método facilmente computado e que será utilizado para implementar a solução do programa.
#Objetivo:
# Criar um programa para calcular e imprimir o endereço-base de um conjunto de chaves.
#Entrada:
# A entrada é composta por uma linha contendo dois valores, que deverão ser transformados em inteiros, 
# K e M, sendo a quantidade de chaves e tamanho da tabela hash, respectivamente.  
# Na sequência serão fornecidos K valores inteiros, um em cada linha.
#Saída:
# Para cada chave seu programa deve produzir uma linha composta pela chave e o endereço-base separados por "->".   
