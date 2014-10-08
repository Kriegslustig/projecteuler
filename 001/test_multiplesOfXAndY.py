import unittest
from calcMultiplesOfXAndY import CalcMultiplesOfXAndY

class TestMultiplesOfXAndY(unittest.TestCase):
	def setUp(self):
		self.x = 3
		self.y = 5
		self.calcMultiplesOfXAndY = CalcMultiplesOfXAndY(self.x, self.y)
		self.calcMultiplesOfXAndY_calc_return = self.calcMultiplesOfXAndY.calc()

	def test_calc(self):
		self.assertTrue(type(self.calcMultiplesOfXAndY_calc_return) == int)
		self.assertRaises(TypeError, self.calcMultiplesOfXAndY.calc, [1,2,3])

	def test_calcMulti(self):
		self.assertTrue(type(self.calcMultiplesOfXAndY._calcMulti(self.x)) == list)
		modflag = True
		for n in self.calcMultiplesOfXAndY._calcMulti(self.x):
			if n % self.x != 0 and modflag:
				modflag = False
		self.assertTrue(modflag)

if __name__ == '__main__':
	unittest.main()