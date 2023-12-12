pizzas = ["burrata","quatro queijos","calabresa"]
friend_pizzas = pizzas[:]
print(pizzas.append("camarão"))
print(friend_pizzas.append("frango com catupiry"))

# mesmo problema que o exercício 1, coloque o nome melhor de variável
# e preste atenção nos espaços
print("minhas pizzas preferidas são:")
for pizzaria in pizzas:
  print(pizzaria.title())

print("As pizzas favoritas do meu amigo são:")
for pizzaria in friend_pizzas:
 print(pizzaria.title())
