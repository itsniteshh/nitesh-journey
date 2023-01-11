#print("HEllo world")

#Write your code below this line 👇
def prime_checker(number):
    
    if number > 1:
        #a function to check prime nos
        for n in range(2, number):
            if number % n == 0:
                print("Not Prime")
                break
            else:
                print("Prime")
                break
    else:
        pass
        

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

