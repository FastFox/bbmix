import csv, math
from datetime import datetime

class Mix():
	bioharness = None
	writer = None
	beddit = None

	def __init__(self):
		print 'Mix init'
		self.writer = csv.writer(open('output.csv', 'w'))
		#columns = ['Timestamp', 'HR', 'BR', 'Activity', 'Acceleration', 'BRAmplitude']
		columns = ['Datetime', 'Minute', 'Avg Bio HR', 'Avg Beddit HR']
		self.writer.writerow( columns )
		self.bioharness = csv.reader(open('2013_03_07-21_52_51_General.csv', 'r'))
		minute = None
		hr = 0
		p = 0.0
		n = 0.0
		start = None
		now = None
		tmpMinute = None

		hr = {}	
		mim = 0.0 # Measurements in the minute

		for i, row in enumerate(self.bioharness):
			if i == 1:
				start = datetime.strptime(row[0], '%d/%m/%Y %H:%M:%S.%f')
				print 'Start', start
			if i != 0:
				if row[1] != '0':
					now = datetime.strptime(row[0], '%d/%m/%Y %H:%M:%S.%f') 
					minute = int(math.floor( (now - start).total_seconds() / 60))
					#print now.strftime('%d/%m/%Y %H:%M')

					if minute == tmpMinute:
						hr[minute] += int(row[1])
						mim += 1.0
						'hoi'
					else:
						if i != 1:
						#print tmpMinute, hr[tmpMinute]
							#print tmpMinute, hr[tmpMinute] / mim
							self.writer.writerow([now.strftime('%d/%m/%Y %H:%M'), tmpMinute, hr[tmpMinute] / mim])
						tmpMinute = minute
						hr[minute] = int(row[1])
						mim = 1.0

		#print hr


					#print i, row[1]
					#self.writer.writerow([row[0], row[1], row[2], row[5], row[6], row[7]])
					#print i, row


			#if row[0] != 'Timestamp':
				#if i == 0:
					#print row[1]
					#'hoi'
				#i += 1
				#hr += 
				#if i == 60:
				#	i = 0
				#minute += 1

			#if row[1] == '0':
			#	n += 1
			#else: 
			#	p += 1
		#print (n / (p + n) ) * 100
		"""	
		self.bioharness = csv.reader(open('2013_03_07-21_52_51_General.csv', 'r'))
		#p = 0
		#n = 0
		for row in self.bioharness:
			i += 1
			if row[1] == '0':
				n += 1
			else: 
				p += 1
		#print n / p
		print (n / (p + n) ) * 100, i
		"""



def main():
	M = Mix()

if __name__ == "__main__":
	main()
