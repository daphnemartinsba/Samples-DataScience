def busca(T, dado, valor=None): 
    k = dado % M
    p = k
    passo = 0
    while tabela[p] != valor and passo < M:
        passo = passo + 1 
        p = (k + passo * 1) % M   
    if tabela[p] == valor:
        return p
    else:
        return None


tabela = {0:14, 1:None, 3:None, 4:None, 5:12, 6:13}
M = len(tabela) 
dado = 19

p = busca(tabela, dado, dado) 
if p != None:
    tabela[p] = None
