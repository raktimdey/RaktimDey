count=0
print("enter your name")
name=input()
for letter in name:
    if(letter in ['A','E','I','O','U']):
        count=count+1
print("You have",count,"Vowels in your name")