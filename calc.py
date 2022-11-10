

co = 1



while co!=0:
	val1 = int(input("Enter First Value :\n"))

	choices = '''
1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulus'''

	print(choices)
	choices = int(input("Enter Choice :\n"))
	if choices not in [1,2,3,4,5]:
		print("Invalid Choice!")
		break
	val2 = int(input("Enter Second Value :\n"))


	if choices == 1:
		res = val1 + val2
		print(res)

	elif choices == 2:
		res = val1 - val2
		print(res)

	elif choices == 3:
		res = val1*val2
		print(res)

	elif choices == 4:
		res = val1/val2
		print(res)

	elif choices == 5:
		res = val1%val2
		print(res)


	p = input("Do you want to Continue? Press 'Y' or 'N'")
	if p in ['Y', 'y']:
		continue
	else:
		break