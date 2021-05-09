import csv
from sys import argv

class Contract():

	def __init__(self, name, start, end):
		self.__name = name
		self.__start = int(start)
		self.__end = int(end) 
		self.__length = end - start
		self.__status = False

	def name(self):
		return self.__name

	def start(self):
		return self.__start

	def end(self):
		return self.__end

	def length(self):
		return self.__length

	def accept(self):
		self.__status = True

	def info(self):
		return self.__name, self.__start, self.__end, self.__status



def parse(path):
	candidates = []

	with open(path) as File:
		register = csv.reader(File)
		for row in register:
			c = Contract(row[0], int(row[1]), int(row[2]))
			candidates.append(c)
#	for c in candidates:
#		print(c.info())
	return candidates


def get_contracts(list):
	"""Algoritmo"""


def write_output(list):
	with open('salida.txt', 'w') as File:
		for candidate in list:
			File.write(candidate.name() + '\n')


def main(argv):
	assert len(argv) == 2

	candidates = parse(argv[1])
	accepted = get_contracts(candidates)
	write_output(accepted)



###Tests###

#parse('ejemplo.csv')
#main(argv)
