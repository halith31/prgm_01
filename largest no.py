m=int(raw_input())
d=int(raw_input())
h=int(raw_input())
if((m>d) and (m>h)):
	print("m")
elif((d>m) and (d>h)):
	print("d")
else:
	print("h")
