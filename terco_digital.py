oracoes = {"Pai Nosso":1, "Ave Maria":10, "Glória":1, "Oh meu Jesus":1}
oracoes_iniciais = {
    "Em Nome do Pai":1,
    "Credo":1,
    "Pai Nosso":1,
    "Ave Maria":3,
    "Glória":1,
    "Oh meu Jesus":1
}

nome = input("Digite seu nome: ")
print(f"\nSeja bem-vindo(a) ao Terço Digital, {nome}!\n")

def rezar(lista_oracoes):
    for item, quantidade in lista_oracoes.items():
        for _ in range(quantidade):
            while True:
                print(f"Reze: {item}")
                entrada = input("Digite 1 para continuar ou 0 para sair: ")

                if entrada in ["0", "1"]:
                    break
                else:
                    print("Entrada inválida!")

            if entrada == "0":
                print(f"\nObrigado por utilizar o Terço Digital, {nome}!")
                return False
    return True

if not rezar(oracoes_iniciais):
    exit()

misterios = [
    "1º Mistério",
    "2º Mistério",
    "3º Mistério",
    "4º Mistério",
    "5º Mistério"
]

for misterio in misterios:
    print(f"\n{misterio}")
    if not rezar(oracoes):
        exit()

print("\nReze: Salve Rainha")
print(f"Terço finalizado! Obrigado por utilizar o Terço Digital, {nome}!")
