def show_messages(lists):
    while lists:
        message=lists.pop()
        print(message)
        send_messages(message)

def send_messages(message):
    sent_message.append(message)

sent_message=[]
lists=['Hello','world']
show_messages(lists)
print(lists)
print(sent_message)