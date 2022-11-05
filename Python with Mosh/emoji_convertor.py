#program to convert symbol emoji to real one

emojis = {
    ":)" :"😥",
    ":(" : "😁"
}
output_msg = ""
input_msg = input("> ").split(" ")

for emo in input_msg:
    output_msg += emojis.get(emo, emo)
    
    
print(output_msg)
