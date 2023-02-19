prompt="enter pizza toppings. enter 'quit' when u finish "
while True:
    topping=input(prompt)
    if topping == "quit":
        break
    else:
        print(f"I'd love to add {topping}")

