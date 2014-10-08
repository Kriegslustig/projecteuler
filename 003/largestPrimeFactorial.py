class LargestPrimeFactorial(object):
	def __init__(self):
		pass

	def isPrime(self, n):
		i = 2
		while i < (n / 2):
			if n % i == 0:
				break
				return False
			i += 1
		return True
