>>> import random
>>> countH=0
>>> countT=0
>>> print("H  T")
H  T
>>> for n in range(0,20):
	num=random.randint(0,1)
	if num==0:
		print("H")
		countH=countH+1
	else:
		print ("  T")
		countT=countT+1
	print(countH,"",countT)

	
  T
0  1
  T
0  2
H
1  2
H
2  2
  T
2  3
  T
2  4
  T
2  5
H
3  5
H
4  5
H
5  5
  T
5  6
  T
5  7
H
6  7
H
7  7
  T
7  8
H
8  8
H
9  8
  T
9  9
  T
9  10
H
10  10
>>> 
