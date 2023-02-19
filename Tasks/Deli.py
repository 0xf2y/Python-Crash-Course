sandwich_orders=["chicken","meat","tuna"]
finished_sandwiches=[]
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
for finished_sand in finished_sandwiches:
        print(finished_sand)