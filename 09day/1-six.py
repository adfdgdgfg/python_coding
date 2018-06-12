ji = 0
ou = 0
 
i = 0
while i < 100:
	print(i)
	if i % 2 == 0:
		ou = ou - i
	else:
		ji = ji + i 
	
	i+=1
print("偶数的和是%d"%ou)
print("奇数的和是%d"%ji)



