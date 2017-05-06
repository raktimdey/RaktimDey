Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
# import is used to make specialty functions available
# These are called modules
import random
import sys
import os
 
# Hello world is just one line of code
# print() outputs data to the screen
print("Hello World")
 
'''
This is a multi-line comment
'''
 
# A variable is a place to store values
# Its name is like a label for that value
name = "Derek"
print(name)
 
# A variable name can contain letters, numbers, or _
# but can't start with a number
 
# There are 5 data types Numbers, Strings, List, Tuple, Dictionary
# You can store any of them in the same variable
 
name = 15
print(name)
 
# The arithmetic operators +, -, *, /, %, **, //
# ** Exponential calculation
# // Floor Division
print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 % 2 =", 5%2)
print("5 ** 2 =", 5**2)
print("5 // 2 =", 5//2)
 
# Order of Operation states * and / is performed before + and -
 
print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)
 
# A string is a string of characters surrounded by " or '
# If you must use a " or ' between the same quote escape it with \
quote = "\"Always remember your unique,"
 
# A multi-line quote
multi_line_quote = ''' just
like everyone else" '''
 
print(quote + multi_line_quote)
 
# To embed a string in output use %s
print("%s %s %s" % ('I like the quote', quote, multi_line_quote))
 
# To keep from printing newlines use end=""
print("I don't like ",end="")
print("newlines")
 
# You can print a string multiple times with *
print('\n' * 5)
 
# LISTS -------------
# A list allows you to create a list of values and manipulate them
# Each value has an index with the first one starting at 0
 
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('The first item is', grocery_list[1])
 
# You can change the value stored in a list box
grocery_list[0] = "Green Juice"
print(grocery_list)
 
# You can get a subset of the list with [min:up to but not including max]
 
print(grocery_list[1:3])
 
# You can put any data type in a a list including a list
other_events = ['Wash Car', 'Pick up Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]
 
print(to_do_list)
 
# Get the second item in the second list (Boxes inside of boxes)
print(to_do_list[1][1])
 
# You add values using append
grocery_list.append('onions')
print(to_do_list)
 
# Insert item at given index
grocery_list.insert(1, "Pickle")
 
# Remove item from list
grocery_list.remove("Pickle")
 
# Sorts items in list
grocery_list.sort()
 
# Reverse sort items in list
grocery_list.reverse()
 
# del deletes an item at specified index
del grocery_list[4]
print(to_do_list)
 
# We can combine lists with a +
to_do_list = other_events + grocery_list
print(to_do_list)
 
# Get length of list
print(len(to_do_list))
 
# Get the max item in list
print(max(to_do_list))
 
# Get the minimum item in list
print(min(to_do_list))
 
# TUPLES -------------
# Values in a tuple can't change like lists
 
pi_tuple = (3, 1, 4, 1, 5, 9)
 
# Convert tuple into a list
new_tuple = list(pi_tuple)
 
# Convert a list into a tuple
# new_list = tuple(grocery_list)
 
# tuples also have len(tuple), min(tuple) and max(tuple)
 
# DICTIONARY or MAP -------------
# Made up of values with a unique key for each value
# Similar to lists, but you can't join dicts with a +
 
super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Mirror Master' : 'Sam Scudder',
                  'Pied Piper' : 'Thomas Peterson'}
 
print(super_villains['Captain Cold'])
 
# Delete an entry
del super_villains['Fiddler']
print(super_villains)
 
# Replace a value
super_villains['Pied Piper'] = 'Hartley Rathaway'
 
# Print the number of items in the dictionary
print(len(super_villains))
 
# Get the value for the passed key
print(super_villains.get("Pied Piper"))
 
# Get a list of dictionary keys
print(super_villains.keys())
 
# Get a list of dictionary values
print(super_villains.values())
 
# CONDITIONALS -------------
# The if, else and elif statements are used to perform different
# actions based off of conditions
# Comparison Operators : ==, !=, >, <, >=, <=
 
# The if statement will execute code if a condition is met
# White space is used to group blocks of code in Python
# Use the same number of proceeding spaces for blocks of code
 
age = 30
if age > 16 :
    print('You are old enough to drive')
 
# Use an if statement if you want to execute different code regardless
# of whether the condition ws met or not
 
if age > 16 :
    print('You are old enough to drive')
else :
    print('You are not old enough to drive')
 
# If you want to check for multiple conditions use elif
# If the first matches it won't check other conditions that follow
 
if age >= 21 :
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive a car')
else :
    print('You are not old enough to drive')
 
# You can combine conditions with logical operators
# Logical Operators : and, or, not
 
if ((age >= 1) and (age <= 18)):
    print("You get a birthday party")
elif (age == 21) or (age >= 65):
    print("You get a birthday party")
elif not(age == 30):
    print("You don't get a birthday party")
else:
    print("You get a birthday party yeah")
 
# FOR LOOPS -------------
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9
for x in range(0, 10):
    print(x , ' ', end="")
 
print('\n')
 
# You can use for loops to cycle through a list
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
 
for y in grocery_list:
    print(y)
 
# You can also define a list of numbers to cycle through
for x in [2,4,6,8,10]:
    print(x)
 
# You can double up for loops to cycle through lists
num_list =[[1,2,3],[10,20,30],[100,200,300]];
 
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])
 
# WHILE LOOPS -------------
# While loops are used when you don't know ahead of time how many
# times you'll have to loop
random_num = random.randrange(0,100)
 
while (random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)
 
# An iterator for a while loop is defined before the loop
i = 0;
while (i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        i += 1
        # Skips to the next iteration of the loop
        continue
 
    i += 1
 
# FUNCTIONS -------------
# Functions allow you to reuse and write readable code
# Type def (define), function name and parameters it receives
# return is used to return something to the caller of the function
def addNumbers(fNum, sNum):
    sumNum = fNum + sNum
    return sumNum
 
print(addNumbers(1, 4))
 
# Can't get the value of rNum because it was created in a function
# It is said to be out of scope
# print(sumNum)
 
# If you define a variable outside of the function it works every place
newNum = 0;
def subNumbers(fNum, sNum):
    newNum = fNum - sNum
    return newNum
 
print(subNumbers(1, 4))
 
# USER INPUT -------------
print('What is your name?')
 
# Stores everything typed up until ENTER
name = sys.stdin.readline()
 
print('Hello', name)
 
# STRINGS -------------
# A string is a series of characters surrounded by ' or "
long_string = "I'll catch you if you fall - The Floor"
 
# Retrieve the first 4 characters
print(long_string[0:4])
 
# Get the last 5 characters
print(long_string[-5:])
 
# Everything up to the last 5 characters
print(long_string[:-5])
 
# Concatenate part of a string to another
print(long_string[:4] + " be there")
 
# String formatting
print("%c is my %s letter and my number %d number is %.5f" % ('X', 'favorite', 1, .14))
 
# Capitalizes the first letter
print(long_string.capitalize())
 
# Returns the index of the start of the string
# case sensitive
print(long_string.find("Floor"))
 
# Returns true if all characters are letters ' isn't a letter
print(long_string.isalpha())
 
# Returns true if all characters are numbers
print(long_string.isalnum())
 
# Returns the string length
print(len(long_string))
 
# Replace the first word with the second (Add a number to replace more)
print(long_string.replace("Floor", "Ground"))
 
# Remove white space from front and end
print(long_string.strip())
 
# Split a string into a list based on the delimiter you provide
quote_list = long_string.split(" ")
print(quote_list)
 
# FILE I/O -------------
 
# Overwrite or create a file for writing
test_file = open("test.txt", "wb")
 
# Get the file mode used
print(test_file.mode)
 
# Get the files name
print(test_file.name)
 
# Write text to a file with a newline
test_file.write(bytes("Write me to the file\n", 'UTF-8'))
 
# Close the file
test_file.close()
 
# Opens a file for reading and writing
test_file = open("test.txt", "r+")
 
# Read text from the file
text_in_file = test_file.read()
 
print(text_in_file)
 
# Delete the file
os.remove("test.txt")
 
# CLASSES AND OBJECTS -------------
# The concept of OOP allows us to model real world things using code
# Every object has attributes (color, height, weight) which are object variables
# Every object has abilities (walk, talk, eat) which are object functions
 
class Animal:
    # None signifies the lack of a value
    # You can make a variable private by starting it with __
    __name = None
    __height = None
    __weight = None
    __sound = None
 
    # The constructor is called to set up or initialize an object
    # self allows an object to refer to itself inside of the class
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
 
    def set_name(self, name):
        self.__name = name
 
    def set_height(self, height):
        self.__height = height
 
    def set_weight(self, height):
        self.__height = height
 
    def set_sound(self, sound):
        self.__sound = sound
 
    def get_name(self):
        return self.__name
 
    def get_height(self):
        return str(self.__height)
 
    def get_weight(self):
        return str(self.__weight)
 
    def get_sound(self):
        return self.__sound
 
    def get_type(self):
        print("Animal")
 
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name, self.__height, self.__weight, self.__sound)
 
# How to create a Animal object
cat = Animal('Whiskers', 33, 10, 'Meow')
 
print(cat.toString())
 
# You can't access this value directly because it is private
#print(cat.__name)
 
# INHERITANCE -------------
# You can inherit all of the variables and methods from another class
 
class Dog(Animal):
    __owner = None
 
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        self.__animal_type = None
 
        # How to call the super class constructor
        super(Dog, self).__init__(name, height, weight, sound)
 
    def set_owner(self, owner):
        self.__owner = owner
 
    def get_owner(self):
        return self.__owner
 
    def get_type(self):
        print ("Dog")
 
    # We can overwrite functions in the super class
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(self.get_name(), self.get_height(), self.get_weight(), self.get_sound(), self.__owner)
 
    # You don't have to require attributes to be sent
    # This allows for method overloading
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound)
        else:
            print(self.get_sound() * how_many)
 
spot = Dog("Spot", 53, 27, "Ruff", "Derek")
 
print(spot.toString())
 
# Polymorphism allows use to refer to objects as their super class
# and the correct functions are called automatically
 
class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()
 
test_animals = AnimalTesting()
 
test_animals.get_type(cat)
test_animals.get_type(spot)
 
spot.multiple_sounds(4)
