message = input(">: ").split(" ")


emojis = {
    ":)": "😊",
    ":(": "😢"
}

new = emojis.get(message[-1])
message[-1] = new


final_msg = " ".join(message)
print(final_msg)
