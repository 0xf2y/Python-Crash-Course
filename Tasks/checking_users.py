current_userss=["leo","gabriel","gabi","thomas","granit"]
new_users=["ben","gabi","thomas","fabio","roberto"]
for user in new_users:
    if user in current_userss:
        print("u will need to enter a new username.")
    else:
        print(f"{user} is available.")