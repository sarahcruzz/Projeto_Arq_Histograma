# (1) importações das bibliotecas


# (2) entrada dos dados
tabela = {"nome" : ["João", "José", "Maria"], "idade" : [25, 29, 15], "nota" : [50, 20, 86]}

# (3) processamento dos dados
# inclusão de um novo aluno: ["Carlos", 20, 60]
tabela["nome"].append("Carlos")
tabela["idade"].append(20)
tabela["nota"].append(60)

# Estraégia: percorrer todo o vetor de notas e gravar a posição de maior valor
tamanho = len(tabela["nota"]) # acha o tamanho do vetoe
contador = range(tamanho) # cria um contador de 0 a tamanho
maior_nota = -1 # nota de partida, em geral, usa-se um valor impossível

posicao = 2

for i in contador:
    nota_atual = tabela["nota"][i] # pega a nota na posição i 
    
    if nota_atual > maior_nota: # testa se a nota atual é maior do que outra anterior
        print(f"A nota atual {nota_atual} é maior do que a anterior {maior_nota  }")
        maior_nota = nota_atual # em caso positivo, atualiza o valor e grava a posição onde ela ocorreu
        posicao = i

# (4) apresentação dos resultados
print(tabela)
print("O conjunto de notas é", tabela["nota"]) # Resposta A
print("a última nota armazenada é", tabela["nota"][-1])
print("O nome do aluno com maior nota é:", tabela["nome"][posicao])