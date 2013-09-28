Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from numpy import *
>>> a = array([1, 2, 3, 4, 5])
>>> a
array([1, 2, 3, 4, 5])
>>> print(a)
[1 2 3 4 5]
>>> A = = [[3, 4, 5], [6, 7, 8], [9, 0, 1]]
SyntaxError: invalid syntax
>>> A = [[3, 4, 5], [6, 7, 8], [9, 0, 1]]
>>> A
[[3, 4, 5], [6, 7, 8], [9, 0, 1]]
>>> print(transpose(A))
[[3 6 9]
 [4 7 0]
 [5 8 1]]
>>> a = matrix(A)
>>> a
matrix([[3, 4, 5],
        [6, 7, 8],
        [9, 0, 1]])
>>> B = [[8],[9],[5]]
>>> A = [[1, -2, 1], [2, 1, -3], [-3, 1, 3]]
>>> a = matrix(A)
>>> b = matrix(B)
>>> linalg.solve(a, b)
matrix([[ 27.2],
        [ 20.6],
        [ 22. ]])
>>> B = [[8],[-99],[5]]
>>> B = [[8],[-9],[5]]
>>> b = matrix(B)
>>> linalg.solve(a, b)
matrix([[ 2.],
        [-1.],
        [ 4.]])
>>> n#otación QR
>>> B = array([(9,4,2),(5,3,1),(2,0,7)])
>>> B
array([[9, 4, 2],
       [5, 3, 1],
       [2, 0, 7]])
>>> Q,R = linalg.qr
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    Q,R = linalg.qr
TypeError: 'function' object is not iterable
>>> Q,R = linalg.qr(B)
>>> Q
array([[-0.85811633,  0.14841033, -0.49153915],
       [-0.47673129, -0.58583024,  0.65538554],
       [-0.19069252,  0.79672913,  0.57346234]])
>>> R
array([[-10.48808848,  -4.86265921,  -3.52781158],
       [  0.        ,  -1.16384941,   5.28809431],
       [  0.        ,   0.        ,   3.68654364]])
>>> ones
<function ones at 0x03445078>
>>> ones(4)
array([ 1.,  1.,  1.,  1.])
>>> ones(4, 2)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    ones(4, 2)
  File "C:\Python33\lib\site-packages\numpy\core\numeric.py", line 149, in ones
    a = empty(shape, dtype, order)
TypeError: data type not understood
>>> ones((1,2))
array([[ 1.,  1.]])
>>> ones((3,2))
array([[ 1.,  1.],
       [ 1.,  1.],
       [ 1.,  1.]])
>>> zeroes((1,2))
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    zeroes((1,2))
NameError: name 'zeroes' is not defined
>>> zero
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    zero
NameError: name 'zero' is not defined
>>> zeros
<built-in function zeros>
>>> zeros((1,2))
array([[ 0.,  0.]])
>>> zeros((4,2))
array([[ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.]])
>>> A = 
