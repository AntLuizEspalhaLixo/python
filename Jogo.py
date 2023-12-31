import random

print("Bem-vindo ao jogo de cálculos do Yaguinho/Yoshi")
print("Você deverá acertar o resultado dos cálculos se não será chamado de burro")
print("Quando desejar sair/rage quit digite: sair")

# inicializando variaveis gerais
encerrar = False
pontuacao = 0
totalrespostas = 0

while (encerrar == False):
    a = random.randint(1,100)
    b = random.randint(1,100)
    operacao = random.choice(["+", "-", "*"])
    pergunta = f"{a} {operacao} {b}"
    print(f"Qual o resultado de: {pergunta}")
    resposta = eval(pergunta)
    respostadousuario = input("Sua resposta: ")
    if respostadousuario == "sair":
        encerrar = True
    else:
        totalrespostas = totalrespostas+1 
        
        if float(respostadousuario) == resposta:
            print("Acertou!")
            pontuacao = pontuacao+1
        else:
            print("Errou...")
else:
      print("sua pontuação foi: ",pontuacao,"/",totalrespostas)
      print("O jogo foi fechado com sucesso!")