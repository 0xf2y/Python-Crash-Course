pizzas=["mahroom","margeata","sauces"]
friend_pizzas=pizzas[:]
pizzas.append("chicken")
friend_pizzas.append("meat")
print("My favorite pizzas are:,")
for pizza in pizzas :
    print(f"\t{pizza}")
print("My friend's favorite pizzas are:,\t")
for friend_pizza in friend_pizzas :
    print(f"\t{friend_pizza}")