import abc


class Charachter(abc.ABC):

	def __init__(self):
		self.info()
		self.weapon_type = None


	@abc.abstractmethod
	def info(self):
		pass


	def set_weapon_behavior(self, weapon='knife'):
		pass





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