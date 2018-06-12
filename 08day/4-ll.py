import random 
i = 0
a = random.randint(1,100)
while i <10:

	c = int(input("请输入1,100的值"))
	if c >a:
		print("值过大")
	elif c <a:
		print("值过小")
	elif c ==a: 
		print("恭喜你，猜对了")
	i = 3

