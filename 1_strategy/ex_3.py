import abc


class Charachter(abc.ABC):

	def __init__(self):
		self.info()
		self.weapon_type = None

	@abc.abstractmethod
	def info(self):
		pass

	def set_weapon_behavior(self, weapon='knife'):
		if weapon=='knife':
			self.weapon_type = KnifeBehavior()
		elif weapon=='bowandarrow':
			self.weapon_type = BowAndArrowBehavior()
		elif weapon=='axe':
			self.weapon_type = AxeBehavior()
		elif weapon=='sword':
			self.weapon_type = SwordBehavior()
		else:
			print("Select either (knife/bowandarrow/axe/sword)")

	def weapon_action(self):
		self.weapon_type.weapon_behavior()


########################################################################################

class Weapon(abc.ABC):

	def __init__(self):
		pass

	abc.abstractmethod
	def weapon_behavior(self):
		pass


class KnifeBehavior(Weapon):

	def __init__(self):
		pass


	def weapon_behavior(self):
		print("Pierced the knife into the heart of the opponent!")


class BowAndArrowBehavior(Weapon):

	def __init__(self):
		pass


	def weapon_behavior(self):
		print("Arrow through the heart of the opponent!")


class AxeBehavior(Weapon):

	def __init__(self):
		pass


	def weapon_behavior(self):
		print("Chopped of the head of the opponent!")


class SwordBehavior(Weapon):

	def __init__(self):
		pass


	def weapon_behavior(self):
		print("Sword through the opponents body!")


########################################################################################

class Queen(Charachter):

	def __init__(self):
		self.set_weapon_behavior('bowandarrow')

	def info():
		print("Queen")


class King(Charachter):

	def __init__(self):
		self.set_weapon_behavior('knife')

	def info():
		print("King")


class Troll(Charachter):

	def __init__(self):
		self.set_weapon_behavior('axe')

	def info():
		print("Troll")


class Knight(Charachter):

	def __init__(self):
		self.set_weapon_behavior('sword')

	def info():
		print("Knight")


if __name__ == '__main__':

	## Testing for Queen ##
	print('*'*10)
	q = Queen()
	q.weapon_action()
	print('*'*10)

	## Testing for King ##
	print('*'*10)
	k = King()
	k.weapon_action()
	print('*'*10)

	## Testing for Troll ##
	print('*'*10)
	t = Troll()
	t.weapon_action()
	print('*'*10)

	## Testing for Knight ##
	print('*'*10)
	kn = Knight()
	kn.weapon_action()
	print('*'*10)