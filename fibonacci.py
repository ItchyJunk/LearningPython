def fibonacii():
	while True:
		try:
			n = int(input('Enter the starting term:'))
			m = int(input('Enter ending term:'))
			break
		except ValueError:
			print ('Please enter a digit:')

	u_zero = 0
	u_one = 1

	for i in range(m):
		if u_zero >= n and u_zero <= m:
			print(u_zero)
			print(u_one)
		if u_zero > m:
			break

		u_zero += u_one
		u_one += u_zero

fibonacii()