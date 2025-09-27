dinheiro = 25
preco_ingresso = 40
carteirinha_estudante = True
passe_livre = False 


pode_entrar = (dinheiro >= preco_ingresso) or (carteirinha_estudante and dinheiro >=preco_ingresso / 2 ) or passe_livre

print(pode_entrar) 