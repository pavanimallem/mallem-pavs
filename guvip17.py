l,r=(raw_input().split())
l=int(l)
r=int(r)
list1=[]
for i in range(1,10000):
	if (i%l==0 and i%r==0):
		list1.append(i)
sorted(list1)
print list1[0]
