import numpy as np

def make_diagonal(x):
	# Your code here
	res=[]
	n=len(x)
	for i in range(n):
		res.append([0]*n)
	for i in range(n):
		res[i][i]=x[i]
	return res
