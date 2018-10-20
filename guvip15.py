string=str(raw_input())
count={}
max=-1
c=''
for s in string:
	if s in count.keys():
		count[s]+=1
	

	else:
		count[s]=1
		
		
for s in string:
	if max < count[s]:
		max=count[s]
		c=s
print(c)
