n=int(raw_input())
list=[int(x) for x in raw_input().split()]
l=[]
for i in range(0,n):
	for j in range(i+1,n):
		if (list[i]==list[j]and list[i] not in l):
			l.append(list[i])
if list[i] in l:
	l.sort()
	print " ".join(map(str,l))
else:
	print "unique"
		
