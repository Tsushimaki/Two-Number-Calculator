a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("What do you want to do? "))
if c == 1:
	print("Answer:" , a+b)
elif c == 2:
	print("Answer:" , a-b)
elif c == 3:
	print("Answer:" , a*b)
else:
	print("Answer:" , a/b)