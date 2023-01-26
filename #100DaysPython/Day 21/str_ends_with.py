def solution(text, ending):
    # your code here...
    
    length = len(ending)
    
    final_length = text.find(ending)
    
    new_word = text[final_length:]
    
    if new_word == ending:
        return True
    else:
        return False


"""    OR """

def solution(text, ending):
    # your code here...
    
    return text.endswith(ending)