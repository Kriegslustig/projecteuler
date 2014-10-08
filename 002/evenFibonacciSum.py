class EvenFibonacciSum(object):
	def __init__(self, thismax = 4000000):
		self.max = thismax

	def calc(self):
		return sum(self._getFibonacciTo())

	def _getFibonacciTo(self):
		returnFib = [1, 2]
		currFib = 3
		while self.max > currFib:
			returnFib.append(currFib)
			currFib = returnFib[len(returnFib) - 1] + returnFib[len(returnFib) - 2]

		return returnFib

def main():
	evenFibonacciSum = EvenFibonacciSum()
	print(evenFibonacciSum.calc())

if __name__ == '__main__':
	main()