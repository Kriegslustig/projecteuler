import unittest
from largestPrimeFactorial import LargestPrimeFactorial

class TestLargestPrimeFactorial(unittest.TestCase):
	def setUp(self):
		self.largestPrimeFactorial = LargestPrimeFactorial()

	def test_calcPrimesTo(self):
	''' This Mehtod calculates all the primes smaller than half of the input '''
		msg = 'calcPrimesTo(20) should return [3, 5, 7, 11, 13, 17]'
		test_calcPrimesTo20 = self.largestPrimeFactorial.calcPrimesTo(20)
		self.assertTrue(test_calcPrimesTo20 == [3, 5, 7, 11, 13, 17], msg)

	def test_calcFactorsOf(self):
	''' This Method should takes a list of integers as the second argument, checks if the first argument is devisable by them and returns the ones that are.'''
		msg = 'calcFactorsOf([1, 2, 5, 7], 20) should return [1, 2, 5]'
		test_calcFactorsOf20 = self.largestPrimeFactorial.calcFactorsOf([1, 2, 5, 7], 20)
		self.assertTrue(test_calcFactorsOf20 == [1, 2, 5], msg)

	def test_calc(self):
	''' This Method is the sort of the factory of largestPrimeFactorial it first uses calcPrimesTo and with the result of that it executes calcFactorsOf. And at last it gets the highest value in the return of calcFactorsOf '''
		msg = 'calc(13185) should return 13185'
		calc13185 = self.largestPrimeFactorial.calc(13185)
		self.assertTrue(calc13185 == 13185, msg)

if __name__ == '__main__':
	unittest.main()