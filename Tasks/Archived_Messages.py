def send_messages(msgs,sent_messages):
    while msgs:
        sent_msg=msgs.pop()
        print(f"Printing message: {sent_msg}")
        sent_messages.append(sent_msg)
def show_messages(msgs,sent_messages):
    print("\nThe following messages have been printed:")
    print(sent_messages)
    print("\nThe original messages :")
    print(msgs)
msgs=["whoami","cd","ls","cat"]
sent_messages=[]
send_messages(msgs[:],sent_messages)
show_messages(msgs[:],sent_messages)
