import unittest
from evenFibonacciSum import EvenFibonacciSum

class TestEvenFibonacciSum(unittest.TestCase):
	def setUp(self):
		self.maxval = 100
		self.evenFibonacciSum = EvenFibonacciSum(self.maxval)

	def test_EvenFibonacciSum_calc(self):
		self.assertTrue(type(self.evenFibonacciSum.calc()) == int)
		self.assertRaises(TypeError, self.evenFibonacciSum.calc, [1,2,3])

	def test_EvenFibonacciSum__getFibonacciTo(self):
		self.evenFibonacciSum__getFibonacciTo = self.evenFibonacciSum._getFibonacciTo()
		self.assertTrue(type(self.evenFibonacciSum__getFibonacciTo) == list)
		self.assertTrue(self.evenFibonacciSum__getFibonacciTo[0:5] == [1,2,3,5,8], 'What ever you did, doesn\'t seem to have much to do with fibonacci')
		lastTwo = []
		for n in self.evenFibonacciSum__getFibonacciTo:
			if len(lastTwo) == 2:
				self.assertTrue(sum(lastTwo) == n)
				lastTwo[0] = lastTwo[1]
				lastTwo[1] = n
			else:
				lastTwo.append(n)

if __name__ == '__main__':
	unittest.main()