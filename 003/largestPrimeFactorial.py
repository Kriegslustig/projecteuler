class LargestPrimeFactorial(object):
	def __init__(self):
		pass

	def _isPrime(self, n):
		i = 2
		while i <= (n / 2):
			if n % i == 0:
				return False
			i += 1
		return True

	def _calcPrimesTo(self, n):
		returnVal = []
		i = 3
		while i < n:
			if self._isPrime(i):
				returnVal.append(i)
			i += 1
		return returnVal

	def _calcFactorsOf(self, thisList, factor):
		returnVal = []
		for item in thisList:
			if factor % item == 0:
				returnVal.append(item)
		return returnVal

	def calc(self, n):
		allFactorialPrimes = self._calcFactorsOf(self._calcPrimesTo(n), n)
		print(allFactorialPrimes)
		return max(allFactorialPrimes)