n=int(raw_input())
list=[int(x) for x in raw_input().split()]
for i in range(0,n):
	if(list.count(i)==1):
		print i
		
