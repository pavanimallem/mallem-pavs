a,b=raw_input().split()
n1=len(a)
n2=len(b)
count=0
if(n1==n2):
  for i in range(n1):
    if(a[i]==b[i]):
      count=count+0
    else:
      count=count+1 
if(count==1):
  print("yes")
else:
  print("no")
