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
		members = list(self.members)
		for i in range(randint(min, max)):
			member = choice(members)
			self.leaders.add(member)
			self.members.remove(member)
			members.remove(member)
		return

	def shuffle(self)->dict:
		'''Randomly assign members to leaders and return the resulting teams'''
		max_members = len(self.members) // len(self.leaders)
		if len(self.members) % len(self.leaders) != 0:
			max_members += 1
		teams = dict()
		for leader in self.leaders:
			teams[leader] = set()
		leaders = list(self.leaders)
		for member in self.members:
			leader = choice(leaders)
			teams[leader].add(member)
			if len(teams[leader]) >= max_members:
				leaders.remove(leader)
		return teams

if __name__ == '__main__':
	test = TeamShuffler()
	assert test.members == set()
	assert test.leaders == set()

	members = {'abc','def','123','zxc','789','jkl','qwe'}
	test.members = set(members)
	assert id(test.members) != id(members)
	assert test.members == members
	assert test.leaders == set()

	num = 2
	test.generate_leaders(num)
	assert len(test.leaders) == num
	assert len(test.leaders) + len(test.members) == len(members)
	for leader in test.leaders:
		assert leader in members

	leaders = set(test.leaders)
	teams = test.shuffle()
	for leader in leaders:
		assert leader in teams

	max_team_size = len(test.members) // len(test.leaders)
	if len(test.members) % len(test.leaders) > 0:
		max_team_size += 1
	for leader in teams:
		assert max_team_size - len(teams[leader]) in (0,1),max_team_size - len(teams[leader])

	teamed_members = set()
	for leader in teams:
		length = len(teamed_members)
		teamed_members |= teams[leader]
		assert length + len(teams[leader]) == len(teamed_members)
	assert len(teamed_members) + len(leaders) == len(members)
	assert teamed_members | leaders == members
