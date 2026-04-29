oracoes = {"Ave Maria":10,"Glória":1,"Oh meu Jesus":1,"Pai Nosso":1,"Mistério":1}
oracoes_iniciais = {"Em Nome do Pai":1,"Credo":1,"Pai Nosso":1,"Ave Maria":3,"Glória":1,"Oh Meu Jesus":1,"Pai-Nosso":1}
terco = True
primeira_parte = True
segunda_parte = True
contador = 0
nome = input("Digite seu nome:")
print()
print(f"Seja bem vindo(a) ao Terço Digital, {nome}!")
print()
print("Para cada Pai Nosso, Ave Maria ou outra oração que você rezar digite 1 para adicionar a contagem.")
print()
while terco:
  while primeira_parte:
    for item, quantidade in oracoes_iniciais.items():
      for i in range(quantidade):
        print(f"Reze: {item}")
        oracao_atual = int(input("Digite 1 para ir para a próxima oração:"))
        contador = contador + oracao_atual
        if contador >= 9:
          primeira_parte = False
  contador = 0
  while segunda_parte:
        for item, quantidade in oracoes.items():
          for i in range(quantidade):
            print(f"Reze: {item}")
            oracao_atual = int(input("Digite 1 para ir para a próxima oração:"))
            contador = contador + oracao_atual
        if contador >= 70:
          print("Reze: Salve Rainha")
          print(f"Terço finalizado! Obrigado por utilizar o Terço Digital, {nome}!")
          segunda_parte = False
          terco = False
