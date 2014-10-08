#!/usr/bin/python

class CalcMultiplesOfXAndY(object):
	def __init__(self, x, y, thismax = 1000):
		self.x = x
		self.y = y
		self.max = thismax

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

def main():
	thisCalc = CalcMultiplesOfXAndY(3, 5)
	print(thisCalc.calc())

if __name__ == '__main__':
	main()