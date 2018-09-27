s1,s2=raw_input().split()
n=len(s1)
m=len(s2)
p=0
c=0
if(m==n):
	for i in range(0,n-1,1):
		if(s1[i]==s1[i+1]):
			p=p+1
		if(s2[i]==s2[i+1]):
			c=c+1
		break
if(p==c):
	print "yes"
else:
    	print "no"
