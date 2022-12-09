"""
emojis = {
    ":)"  :"😊",
    ":(" : "😢"
}
output = ""
user_input = input("> ").split()

for emo in user_input:
    output += emojis.get(emo, emo) + " "
        
        
print(output)
"""
output = ""

stri = ("i love you dadi")

new_str = stri.split()
for words in new_str:
    output += words.upper()

print(output)

