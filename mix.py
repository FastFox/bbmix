import csv

class Mix():
	bioharness = None

	def __init__(self):
		print 'Mix init'
		self.bioharness = csv.reader(open('2012_04_23-02_52_33_General.csv', 'r'))
		i = 0
		for row in self.bioharness:
			if i == 0:
				print row
			i += 1
			if i == 60:
				i = 0

def main():
	M = Mix()

if __name__ == "__main__":
	main()
