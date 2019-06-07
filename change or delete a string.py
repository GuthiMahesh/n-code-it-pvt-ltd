my_string = 'programiz'
my_string[5] = 'a'
...
# TypeError: 'str' object does not support item assignment
my_string = 'Python'
# >>> my_string
'Python'
# We cannot delete or remove characters from a string. But deleting the string entirely is possible using the keyword del.

del my_string[1]
...
# TypeError: 'str' object doesn't support item deletion
del my_string
my_string
...
# NameError: name 'my_string' is not defined