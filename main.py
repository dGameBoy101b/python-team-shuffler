from CSVReader import CSVReader
from TeamShuffler import TeamShuffler
from sys import argv

def main(*args):
	if len(args) == 2:
		csv = CSVReader(args[1])
		members = csv.read_line()
		leaders = csv.read_line()
		csv.close()
		if len(leaders) == 1:
			try:
				leaders = int(leaders[0])
			except ValueError:
				pass
		shuffler = TeamShuffler(members)
		if isinstance(leaders, int):
			shuffler.generate_leaders(leaders)
		else:
			shuffler.leaders = leaders
		print_teams(shuffler.shuffle())
		return
		
def print_teams(teams:dict):
	for leader in teams:
		print(leader)
		for member in teams[leader]:
			print(f'\t{member}')
	return

if __name__ == '__main__':
	main(*argv)
