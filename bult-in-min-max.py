In [1]: def maximum(value1, value2, value3):
   ...:    ...:     """Return the maximum of three values."""
   ...:    ...:     max_value = value1
   ...:    ...:     if value2 > max_value:
   ...:    ...:         max_value = value2
   ...:    ...:     if value3 > max_value:
   ...:    ...:         max_value = value3
   ...:    ...:     return max_value
   ...: 

In [2]: maximum(12, 27,36)
Out[2]: 36

In [3]: maximum(12.3, 45.6, 9.7)
Out[3]: 45.6

In [4]: maximum('yellow', 'red', 'orange')
Out[4]: 'yellow'

In [5]: maximum(13.5, -3, 7)
Out[5]: 13.5

In [6]: min(15, 9, 27, 14)
Out[6]: 9
