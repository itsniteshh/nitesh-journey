msgs = ["hello", "Good mrng", "bonjour"]
sent_msg = []

def send_msgs(message, sent_msg):
    #a function to send msgs from the list and add to a send list
    while msgs:
        #while loop to automate the repeting task
        sending_msg = msgs.pop()
        print(f"Currently sending the message {sending_msg}")    
        sent_msg.append(sending_msg)
        
def show_sent_msgs(sent_msgs):
    #func to show sent msgs
    for msgs in sent_msgs:
        print(msgs)

send_msgs(msgs, sent_msg)
show_sent_msgs(sent_msg)

