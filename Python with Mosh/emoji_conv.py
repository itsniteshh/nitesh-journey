emojis = {
    ":)"  :"😊",
    ":(" : "😢"
}
output = ""
user_input = input("> ").split()

for emo in user_input:
    output += emojis.get(emo, emo) + " "
        
        
print(output)