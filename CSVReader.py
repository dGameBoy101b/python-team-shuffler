from io import SEEK_END, SEEK_SET
from os import remove

class CSVReader():
	'''A class used to read from CSV files'''

	SEP = ','
	'''The value separator'''

	def __init__(self, path:str=None):
		self._file = None
		if path is None:
			return
		if not isinstance(path, str):
			path = str(path)
		self.open(path)
		return

	def __del__(self):
		self.close()
		return

	def close(self):
		'''Close the currently open CSV file if one is open'''
		if self._file is not None:
			self._file.close()
		self._file = None
		return

	def open(self, path:str):
		'''Open the CSV file pointed to by the given path'''
		if not isinstance(path, str):
			path = str(path)
		if not path.endswith('.csv'):
			raise ValueError(f'Cannot open a file that is not a csv file: {path}')
		if not self.is_open():
			self.close()
		self._file = open(path, 'rt')
		return

	def is_open(self)->bool:
		'''Does this have a CSV file open'''
		return self._file is not None

	def is_eof(self)->bool:
		'''Is the currently open CSV file at its end'''
		pos = self._file.tell()
		self._file.seek(0, SEEK_END)
		end_pos = self._file.tell()
		self._file.seek(pos, SEEK_SET)
		return pos == end_pos
	
	def read_line(self)->list[str]:
		'''Read and return one line of values'''
		if not self.is_open():
			raise RuntimeError('No CSV file open')
		if self.is_eof():
			raise EOFError('The CSV file has no more lines')
		line = self._file.readline().removesuffix('\n')
		if CSVReader.SEP not in line:
			return []
		values = line.split(CSVReader.SEP)
		return values

	def read_all(self)->list[list[str]]:
		'''Read and return all remaining lines of values'''
		if self._file is None:
			raise RuntimeError('No CSV file open')
		lines = list()
		while not self.is_eof():
			lines.append(self.read_line())
		return lines

if __name__ == '__main__':
	test = CSVReader()
	assert not test.is_open()
	assert test._file == None
	del test

	path = './test.csv'
	lines = [['abc','123','','def'],[],['qwerty','1234567890'],['jkl','zxcvbnm','']]
	with open(path, 'wt') as file:
		file.write(''.join([','.join(line)+'\n' for line in lines]))
	test = CSVReader(path)
	assert test.is_open()
	assert not test.is_eof()
	assert test.read_line() == lines[0]
	assert test.is_open()
	assert not test.is_eof()
	assert test.read_line() == lines[1]
	assert test.is_open()
	assert not test.is_eof()
	assert test.read_all() == lines[2:]
	assert test.is_open()
	assert test.is_eof()
	test.close()
	assert not test.is_open()
	del test
	remove(path)
