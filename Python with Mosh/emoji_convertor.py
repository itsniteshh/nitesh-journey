#program to convert symbol emoji to real one

emojis = {
    ":)" :"😥",
    ":(" : "😁"
}

input_msg = input("> ").split(" ")

for emo in input_msg:
    for keys in emojis:
        if emo == keys:
            