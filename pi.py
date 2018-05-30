def method1():
	"""
	Find first x digits of pi
	"""

	numerator = 1
	denominator = 1

	#Make sure the input is int
	while True:
		try:
			precision = int(input('How many digits did you want?'))
			break
		except ValueError:
			print('Please try a valid number')

	total = 0
	n = 0

	while n<1000000:
		"""
		Using Leibniz formula for Pi
		https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
		"""
		total += (-1)**(n) * (numerator/denominator)
		n += 1
		denominator += 2

	pi = total*4

	#printing x digits based on user input. Here x = precision
	return '{:.{p}f}'.format(pi,p=precision)


def method2():
	total = 2
	for i in range(1,10000000):
		total *= (4*(i**2))/((4*i**2)-1)

	return total

print(method1())

print(method2())