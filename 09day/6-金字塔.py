
i = 1
km=float(input("请输入多少公里"))
money = 0
while i <= 30:
	j = 1
	if km == 0:
		breake
	while j <= 2:
		if money < 100:
			if km < 6:
				print("3元")
			elif km > 6 and  km <= 12:
				print("4元")
			elif km > 12 and km <= 22:
				print("5元")
			elif km > 32:
				print(km-32)%20 


















 
