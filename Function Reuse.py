Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /Users/rkhatu/Documents/Triangle.py =================
>>> semiperimeter(3, 4, 5)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    semiperimeter(3, 4, 5)
  File "/Users/rkhatu/Documents/Triangle.py", line 37, in semiperimeter
    return perimeter(side1 + side2 + side3) / 2
TypeError: perimeter() missing 2 required positional arguments: 'side2' and 'side3'
>>> 
================= RESTART: /Users/rkhatu/Documents/Triangle.py =================
>>> semiperimeter(3, 4, 5)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    semiperimeter(3, 4, 5)
  File "/Users/rkhatu/Documents/Triangle.py", line 38, in semiperimeter
    return perimeter(side1 + side2 + side3) / 2
TypeError: perimeter() missing 2 required positional arguments: 'side2' and 'side3'
>>> 
========================== RESTART: /Users/rkhatu/Documents/Triangle.py ==========================
>>> semiperimeter(3, 4, 5)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    semiperimeter(3, 4, 5)
  File "/Users/rkhatu/Documents/Triangle.py", line 38, in semiperimeter
    return perimeter(side1 + side2 + side3) / 2
TypeError: perimeter() missing 2 required positional arguments: 'side2' and 'side3'
>>> 
========================== RESTART: /Users/rkhatu/Documents/Triangle.py ==========================
>>> semiperimeter (3, 4, 5)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    semiperimeter (3, 4, 5)
  File "/Users/rkhatu/Documents/Triangle.py", line 37, in semiperimeter
    return perimeter(side1 + side2 + side3) / 2
TypeError: perimeter() missing 2 required positional arguments: 'side2' and 'side3'
>>> 
========================== RESTART: /Users/rkhatu/Documents/Triangle.py ==========================
>>> perimeter(3, 4, 5)
12
>>> semiperimeter(3, 4, 5)
6.0
>>> semiperimeter( 10.5, 6, 9.3)
12.9
>>> max(area(3.8, 7.0), area(3.5, 6.8))
13.299999999999999
>>> area(3.8, 7.0)
13.299999999999999
>>> area(3.5, 6.8)
11.9
>>> 