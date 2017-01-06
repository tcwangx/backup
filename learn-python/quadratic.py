import math
def quadratic(a,b,c):
	if a>0 or a<0 :
		x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
		x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
		return x1,x2
	else:
		print("error")
		return
