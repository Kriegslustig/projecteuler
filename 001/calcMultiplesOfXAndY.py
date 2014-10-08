class CalcMultiplesOfXAndY:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.max = 1000

	def calc(self):
		self.multiX = self._calcMulti(self.x)
		self.multiY = self._calcMulti(self.y)
		return sum(self.multiX + self.multiY)

	def _calcMulti(self, n):
		returnVal = []
		i = 0
		while i * n < self.max:
			returnVal.append(i * n)
			i += 1
		return returnVal

# if __name__ == '__main__':
# 	thisCalc = CalcMultiplesOfXAndY(3, 5)
# 	print thisCalc.calc()