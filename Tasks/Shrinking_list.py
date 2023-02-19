from operator import le


Guests=["roberto","carlos","junior"]
print("we u found a bigger dinner table.")
Guests.append("Mustafa")
Guests.insert(3,"Assheaf")
Guests.insert(0,"nour")
print(Guests)
for Guest in Guests :
    print(f"hello, {Guest}!!")
print("I can invite only two people for dinner.")
print(f" I am sorry I can't invite u to dinner, {Guests.pop().title()}")
print(f" I am sorry I can't invite u to dinner, {Guests.pop().title()}")
print(f" I am sorry I can't invite u to dinner, {Guests.pop().title()}")
print(f" I am sorry I can't invite u to dinner, {Guests.pop().title()}")
print(Guests)
print(f"{Guests[0]} & {Guests[1]} ,u're still invited.")
del Guests[0]
del Guests[0]
print(Guests)
print(len(Guests))