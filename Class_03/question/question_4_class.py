import math
class Factorizer:
	def __init__(self, n):
		self.number = n

	def print_factorization(self, arr):
		s = str(self.number) + '='
		for i in range(len(arr)-1):
			s += str(arr[i]) + '*'
		s += str(arr[len(arr)-1])
		print(s)

	def print_all_factorizations(self, n, min_factor, arr):
		for i in range(min_factor, int(math.sqrt(n)+1)):
			if n % i == 0:
				arr.append(i)
				self.print_all_factorizations(int(n/i), i, arr)
				arr.pop()
		arr.append(n)
		self.print_factorization(arr);
		arr.pop()

	def find_factorizations(self):
		arr = []
		self.print_all_factorizations(self.number, 2, arr)

n = input()
f = Factorizer(int(n))
f.find_factorizations()
