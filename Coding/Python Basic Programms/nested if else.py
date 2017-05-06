char=input()
if ord(char)>=65 and ord(char)<=90:
    print("You entered an upper case Alpha")
    if char in ['A','E','I','O','U']:
        print("you entered a vowel")
    else:
        print("you entered a consonant")
elif ord(char)>=97 and ord(char)<=122:
     print("You entered an Lower case Alpha")
     if char in ['a','e','i','o','u'] :
        print("you entered a vowel")
     else:
        print("you entered a consonant")
else:
    print("Fuck You")
