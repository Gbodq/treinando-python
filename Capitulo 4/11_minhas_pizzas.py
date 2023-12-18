pizzas = ["burrata","quatro queijos","calabresa"]
friend_pizzas = pizzas[:]
print(pizzas.append("camarão"))
print(friend_pizzas.append("frango com catupiry"))


print("minhas pizzas preferidas são:")
for pizza in pizzas:
    print(pizza.title())

print("As pizzas favoritas do meu amigo são:")
for pizza in friend_pizzas:
   print(pizza.title())
