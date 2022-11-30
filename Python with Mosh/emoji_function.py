global output = ""
user_input = input(">").split() 

def emoji_convertor():
    #function to convert symbols to emojis
    emojis = {  
        ":)"  :"😊",
        ":(" : "😢"
    }
    
    for words in user_input:
        output += emojis.get(words, words) + " "
        return output
        
  
emoji_convertor()
    


