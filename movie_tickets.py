prompt="please enter your age !!"
while True:
    age=int(input(prompt))
    if age < 3:
        print(" the ticket is free")
    elif age > 3 and age <12 :
        print("the ticket is $10")
    elif age > 12:
        print("the ticket is $15")