Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20
>>> a+=30
>>> a%=3
>>> a
2
>>> True*False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3)and(7<4)or (18==3))and (9>3)
False
>>> True is False
False
>>> ((True==False)or(False>True))and(False<=True)
False
>>> s1 = "Nice to have it "
>>> s2 = "here"
>>> s=s1+s2
>>> s
'Nice to have it here'
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2]
['hello']
>>> 
>>> a.insert(0,'s1')
>>> a.insert(7,'s2')
>>> a
['s1', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 's2']
>>> 
>>> n = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]
>>> for i in n:
	if n%2==0 and n<=237:
		print(n)

		
Traceback (most recent call last):
  File "<pyshell#30>", line 2, in <module>
    if n%2==0 and n<=237:
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> x = set(["White", "Black", "Red"])
>>> y = set(["Red", "Green"])
>>> print(x-y)
{'Black', 'White'}
>>> n=5
>>> s=n+n*n+n*n*n
>>> s
155
>>> n=5
>>> t=n**1+n**2+n**3
>>> t
155
>>> 