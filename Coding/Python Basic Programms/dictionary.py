Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #dictionary problems
>>> address={}
>>> address=["Raktim"]="luxmibazar,dhaka"
SyntaxError: can't assign to literal
>>> address["Raktim"]="luxmibazar,dhaka"
>>> address=["Joy"]="Shakaribazar,dhaka"
SyntaxError: can't assign to literal
>>>  address["Joy"]="Shakaribazar,dhaka"
 
SyntaxError: unexpected indent
>>> address["Joy"]="Shakaribazar,dhaka"
>>> print(address)
{'Raktim': 'luxmibazar,dhaka', 'Joy': 'Shakaribazar,dhaka'}
>>> 

>>> print(address)
{'Raktim': 'luxmibazar,dhaka', 'Joy': 'Shakaribazar,dhaka'}
>>> #another method
>>> new={'raktim':'dhaka','joy':700}
>>> new
{'raktim': 'dhaka', 'joy': 700}
>>> address.keys()
dict_keys(['Raktim', 'Joy'])
>>> address.values()
dict_values(['luxmibazar,dhaka', 'Shakaribazar,dhaka'])
>>> 
