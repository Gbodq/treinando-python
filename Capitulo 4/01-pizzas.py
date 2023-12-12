pizzas = ["burrata","quatro queijos","calabresa"]
# você está iterando por sabores de pizza, e não por pizzarias
# o correto seria: for pizza in pizzas:
for pizzaria in pizzas:
# sempre dê pelo menos 4 espaços em branco ao criar um novo escopo
# dessa forma o código fica mais legível
# para isso utilize o tab
# desafio: reescreva para funcionar da mesma forma, chamando a função title() apenas 1 vez 
 print(pizzaria.title())
 print("Gosto de pizza de " + pizzaria.title())

print("Eu realmente adoro pizza!") 