str ="老王"
'''
for i in str:
	print(i)
'''
#range
''' for i in range (起开始值，终止值，步长）
:
'''
#random,randit 有头有尾
#range（有头无尾1）


for i in range(0,5):
	num=int(input("请输入本次抓娃娃需要多少秒(1~60)"))
	if num > 30:
		print("时间到了，机器自动抓给你")
	else:
		print("你次用了%d秒抓了一下"%num)
		continue
	print("你本次用了%d秒抓了一下"%num)


