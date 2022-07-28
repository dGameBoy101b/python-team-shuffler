class CSVReader():
	'''A class used to read from CSV files'''

	def __init__(self, path:str=None):
		if path is None:
			self.file = None
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
		if self.file is not None:
			self.file.close()
		return

	def open(self, path:str):
		'''Open the CSV file pointed to by the given path'''
		if not isinstance(path, str):
			path = str(path)
		if not path.endswith('.csv'):
			raise ValueError(f'Cannot open a file that is not a csv file: {path}')
		if self.path is not None:
			self.close()
		self.file = open(path, 'rt')
		return

	def is_open(self)->bool:
		'''Does this have a CSV file open'''
		return self.file is not None

	def is_readable(self)->bool:
		'''Does this have a CSV file open and is that file not at its end'''
		return self.is_open() and self.file.readable()
	
	def read_line(self)->list[str]:
		'''Read and return one line of values'''
		if self.file is None:
			raise RuntimeError('No CSV file open')
		if not self.file.readable():
			raise EOFError('CSV file is not readable')
		return self.file.readline().split(',')

	def read_all(self)->list[list[str]]:
		'''Read and return all remaining lines of values'''
		if self.file is None:
			raise RuntimeError('No CSV file open')
		lines = list()
		while self.file.readable():
			lines.append(self.readline())
		return lines