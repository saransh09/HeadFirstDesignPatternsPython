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

	def weapon_action(self):
		self.weapon_type.weapon_behavior()

	def info():
		print("This is the queen")




if __name__ == '__main__':

	q = Queen()
	q.weapon_action()