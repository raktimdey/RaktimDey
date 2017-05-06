Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=15
>>> a++
SyntaxError: invalid syntax
>>> a=15
>>> 1=4
SyntaxError: can't assign to literal
>>> 1=13
SyntaxError: can't assign to literal
>>> a=1
>>> a=1
>>> a++
SyntaxError: invalid syntax
>>> a=a
>>> 
>>> a=a
>>> a==a
True
>>> a!=a
False
>>> 
=============================== RESTART: Shell ===============================
>>> a=10
>>> bin(a)
'0b1010'
>>> b=2
>>> bin(a&b)
'0b10'
>>> #binary additon
>>> bin(a&b)
'0b10'
>>> bin(a|b)
'0b1010'
>>> bin(a^b)
'0b1000'
>>> a=True
>>> b=False
>>> a and b
False
>>> a or b
True
>>>  
