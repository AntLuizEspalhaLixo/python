import random

a = random.randint(1,8)
b = random.randint(1,8)
c = ("a", ["+"], ["-"], ["*"], "b")
operacao = random.choice(["+", "-", "*"])
pergunta = f"Qual o resultado de: {a} {operacao} {b}?"
c = eval(pergunta) 
encerrar = False
while (encerrar == False):
	if "resposta" == "sair":
		encerrar = True
	else:
		if operacao == resposta:
			print("Acertou!")
		else:
			print("Errado...")
else:
      print("O jogo foi fechado com sucesso!")