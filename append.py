import numpy as np #importing numpy as np
a=input("enter the array a")#enter the element in the array a
b=input("enter the array b")#enter the element in the array b
print "the elements in array a \n",a
d=np.append(a,b)#append using numpy
print "elements of array a",d
for i in range(0,len(b)):
	if(b[i]>=0):
		a.append(b[i])
print"the element in array a removing negative numbers",a



