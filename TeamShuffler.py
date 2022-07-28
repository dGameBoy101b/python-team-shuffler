from random import choice, randint

class TeamShuffler():
	'''A class used to shuffle teams'''

	def __init__(self, members:set=set(), leaders:set=set()):
		self.leaders = set(leaders)
		self.members = set(members)
		return

	def generate_leaders(self, max:int, min:int=None):
		'''Randomly pick leaders from the list of members'''
		if not isinstance(max, int):
			max = int(max)
		if max < 1:
			raise ValueError(f'The maximum number of leaders must be positive: {max}')
		if len(self.members) < max:
			raise ValueError(f'Insufficient members ({len(self.members)}) available to pick leaders from: {max}')
		if min is None:
			min = max
		if not isinstance(min, int):
			min = int(min)
		if min < 1:
			raise ValueError(f'The minimum number of leaders must be positive: {min}')
		if min > max:
			raise ValueError(f'The minimum number of leaders ({min}) must not be greater than the maximum ({max})')
		self.leaders = set()
		for i in range(randint(min, max)):
			member = choice(self.members)
			self.leaders.add(member)
			self.members.remove(member)
		return

	def shuffle(self)->dict:
		'''Randomly assign members to leaders and return the resulting teams'''
		max_members = len(self.members) / len(self.leaders)
		if len(self.members) % len(self.leaders) != 0:
			max_members += 1
		teams = dict()
		for leader in self.leaders:
			teams[leader] = set()
		leaders = set(self.leaders)
		for member in self.members:
			leader = choice(leaders)
			teams[leader].add(member)
			if len(teams[leader]) >= max_members:
				leaders.remove(leader)
		return teams
