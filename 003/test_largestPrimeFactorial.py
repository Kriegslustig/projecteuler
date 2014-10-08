import unittest
from largestPrimeFactorial import LargestPrimeFactorial

class TestLargestPrimeFactorial(unittest.TestCase):
	def setUp(self):
		self.largestPrimeFactorial = LargestPrimeFactorial()

	def test__isPrime(self):
		'''
			_isPrime(7)
			This Method checks if a number is a prime
		'''
		msgFalse = 'This is not a prime: '
		msgTrue = 'This is a prime: '
		self.assertTrue(self.largestPrimeFactorial._isPrime(7), msgTrue + str(7))
		self.assertFalse(self.largestPrimeFactorial._isPrime(15), msgFalse + str(15))
		self.assertFalse(self.largestPrimeFactorial._isPrime(4), msgFalse + str(4))

	def test__calcPrimesTo(self):
		'''
			_calcPrimesTo(20)
			uses _isPrime
			This Mehtod calculates all the primes smaller than half of the input
		'''
		msg = ' _calcPrimesTo(20) should return [3, 5, 7, 11, 13, 17, 19]'
		test_calcPrimesTo20 = self.largestPrimeFactorial._calcPrimesTo(20)
		self.assertTrue(test_calcPrimesTo20 == [3, 5, 7, 11, 13, 17, 19], msg)

	def test__calcFactorsOf(self):
		'''
			_calcFactorsOf([1, 2, 5, 7], 20)
			This Method should takes a list of integers as the second argument, checks if the first argument is devisable by them and returns the ones that are.
		'''
		msg = '_calcFactorsOf([1, 2, 5, 7], 20) should return [1, 2, 5]'
		test__calcFactorsOf20 = self.largestPrimeFactorial._calcFactorsOf([1, 2, 5, 7], 20)
		self.assertTrue(test__calcFactorsOf20 == [1, 2, 5], msg)

	def test_calc(self):
		'''
			calc(13185)
			This Method is the sort of the factory of largestPrimeFactorial it first uses calcPrimesTo and with the result of that it executes calcFactorsOf. And at last it gets the highest value in the return of calcFactorsOf
		'''
		msg = 'calc(13185) should return 13185'
		calc13185 = self.largestPrimeFactorial.calc(13185)
		self.assertTrue(calc13185 == 13185, msg)

if __name__ == '__main__':
	unittest.main()