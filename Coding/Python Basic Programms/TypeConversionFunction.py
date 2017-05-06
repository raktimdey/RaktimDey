Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> int(5.67574)
5
>>> float(6)
6.0
>>> double(5)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    double(5)
NameError: name 'double' is not defined
>>> float *4
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    float *4
TypeError: unsupported operand type(s) for *: 'type' and 'int'
>>> 
=============================== RESTART: Shell ===============================
>>> int("Raktim")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("Raktim")
ValueError: invalid literal for int() with base 10: 'Raktim'
>>> a=str(5600)
>>> a
'5600'
>>> a=str("raktim")
>>> a
'raktim'
>>> a=str(7400)
>>> a
'7400'
>>> a[2]
'0'
>>> tuple("this is a string")
('t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g')
>>> tuple[1]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    tuple[1]
TypeError: 'type' object is not subscriptable
>>> list("this is a list")
['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'l', 'i', 's', 't']
>>> list[1]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list[1]
TypeError: 'type' object is not subscriptable
>>> chr(65)
'A'
>>> chr(55)
'7'
>>> #find ASCII VAlUES
>>> chr(2)
'\x02'
>>> chr(t)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    chr(t)
NameError: name 't' is not defined
>>> chr(53)
'5'
>>> 
chr('a')
Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    chr('a')
TypeError: an integer is required (got type str)
>>> ord('a')
97
>>> hex(4500)
'0x1194'
>>> oct(4500)
'0o10624'
>>> dec(4500)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dec(4500)
NameError: name 'dec' is not defined
>>> bin(42)
'0b101010'
>>> 
