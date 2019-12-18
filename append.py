#code to append one array into  another arrary
import numpy as np
x=input('enter the array 1:')
y=input('enter the array 2:')
for i in range(0,len(y)):
	x.append(y[i])
print x

