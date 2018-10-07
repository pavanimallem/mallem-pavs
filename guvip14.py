s=int(raw_input())
string=raw_input()
l=len(string)
for i in "aeiouAEIOU":
	string=string.replace(i,"")
print string[::-1]
	
