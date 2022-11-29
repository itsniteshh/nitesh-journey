emojis = {
    ":)"  :"😊",
    ":(" : "😢"
}
output = ""
user_input = input("> ").split()

for emo in user_input:
    if emo in emojis.keys():
        output += emojis.get(emo)
        print(output)
