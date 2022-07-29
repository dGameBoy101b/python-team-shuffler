from CSVReader import CSVReader
from TeamShuffler import TeamShuffler

class PythonTeamShuffler():

	def __init__(self):
		self.shuffler = TeamShuffler()
		return

	def interactive_loop(self):
		'''Enter an interactive loop which does not exit until commanded to by the user'''
		while True:
			args = input(">>> ").split(' ')
			try:
				if args[0] == 'exit':
					return
				elif args[0] == 'shuffle':
					self.shuffle()
				elif args[0] == 'load':
					self.load_data(args[1])
				else:
					raise RuntimeError(f'Command not recognised: {args[0]}')
			except Exception as x:
				print(f'{type(x)}: {x}')

	def load_data(self, path:str):
		'''Load member and leader information from a file'''
		csv = CSVReader(path)
		members = csv.read_line()
		leaders = csv.read_line()
		csv.close()
		self.interpret_args(members, leaders)
		return
	
	def shuffle(self):
		'''Print the teams produced by the current shuffler'''
		self.print_teams(self.shuffler.shuffle())
		return

	def interpret_args(self, members:list, *leaders):
		'''Set up the team shuffler from the given arguments for members and leaders'''
		self.shuffler.members = set(members)
		max_num_leaders = None
		min_num_leaders = None
		try:
			max_num_leaders = int(leaders[0])
			if len(leaders) > 1:
				min_num_leaders = int(leaders[1])
		except (TypeError, ValueError):
			pass
		if max_num_leaders is None:
			self.shuffler.leaders = set(leaders[0])
		else:
			self.shuffler.generate_leaders(max_num_leaders, min_num_leaders)
		self.print_shuffler_state()
		return

	def print_teams(self, teams:dict):
		'''Print the given dictionary of teams'''
		for leader in teams:
			print(f'{leader}: {", ".join(teams[leader])}')
		return

	def print_shuffler_state(self):
		'''Print information regarding the current state of the shuffler'''
		print(f'Members: {", ".join(self.shuffler.members)}')
		print(f'Leaders: {", ".join(self.shuffler.leaders)}')
		return

if __name__ == '__main__':
	try:
		exit_code = PythonTeamShuffler().interactive_loop()
	except Exception as x:
		exit_code = x
	exit(exit_code)
