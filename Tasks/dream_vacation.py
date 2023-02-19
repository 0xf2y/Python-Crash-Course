polling_status=True
while polling_status:
    dream_vacation={}
    user=input("what is your name ?")
    place=input("If you could visit one place in the world, where would you go?")
    dream_vacation[user]=place
    repeat=input("do you want to add another place ? (yes or no)")
    if repeat == "no" :
        polling_status=False
print("\npolling results are:")
print(f"{user} dream vacation is {place}")
