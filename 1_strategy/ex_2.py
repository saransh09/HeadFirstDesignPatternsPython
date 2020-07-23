import abc


class Duck(abc.ABC):

	def __init__(self):
		self.fly_behavior = None
		self.quack_behavior = None

	@abc.abstractmethod
	def info(self):
		pass

	def fly(self):
		if self.fly_behavior is not None:
			self.fly_behavior.fly()
		else:
			print("Fly property not defined properly")

	def quack(self):
		if self.quack_behavior is not None:
			self.quack_behavior.quack()
		else:
			print("Quack property not defined properly")

	def set_fly_property(self, flies='yes'):
		
		if flies=='yes':
			self.fly_behavior = CanFly()
		elif flies=='no':
			self.fly_behavior = CannotFly()
		elif flies=='rocket':
			self.fly_behavior = CanFlyRocket()
		else:
			print("The only valid 'flies' property values are (yes/no/rocket)")

	def set_quack_property(self, quack_type='quack'):

		if quack_type=='quack':
			self.quack_behavior = Quack()
		elif quack_type=='squeek':
			self.quack_behavior = Squeek()
		elif quack_type=='mute_quack':
			self.quack_behavior = MuteQuack()
		else:
			print("The only valid quack_type property values are (quack/squeek/mute_quack)") 



######################### Flying abstract meta class --> Interface for Python ###########################

class QuackBehavior(abc.ABC):

	def __init__(self):
		pass

	@abc.abstractmethod
	def quack(self):
		pass


class Quack(QuackBehavior):

	def __init__(self):
		pass

	def quack(self):
		print("Quack Quack!")


class Squeek(QuackBehavior):

	def __init__(self):
		pass

	def quack(self):
		print("Squeek Squeek!")


class MuteQuack(QuackBehavior):

	def __init__(self):
		pass

	def quack(self):
		print("Mute Quack!")


##########################################################################################################



######################### Flying abstract meta class --> Interface for Python ###########################

class FlyBehavior(abc.ABC):

	def __init__(self):
		pass

	@abc.abstractmethod
	def fly(self):
		pass


class CanFly(FlyBehavior):

	def __init__(self):
		pass

	def fly(self):
		print("Flying in the air")


class CannotFly(FlyBehavior):

	def __init__(self):
		pass

	def fly(self):
		print("I cannot fly you dummy")


class CanFlyRocket(FlyBehavior):

	def __init__(self):
		pass

	def fly(self):
		print("Flying like a rocket")


##########################################################################################################


################################## Defining the specific duck types ######################################

class MallardDuck(Duck):

	def __init__(self):
		self.set_fly_property('yes')
		self.set_quack_property('quack')

	def info(self):
		print("This is a Mallard Duck!")


class RubberDuck(Duck):

	def __init__(self):
		self.set_fly_property('no')
		self.set_quack_property('squeek')

	def info(self):
		print("This is a Rubber Duck!")

##########################################################################################################




if __name__ == '__main__':

	print('*'*10)
	## Test for Mallard Duck ##
	md = MallardDuck()
	md.info()
	md.quack()
	md.fly()
	print('*'*10)

	print('*'*10)
	## Test for Rubber Duck ##
	rd = RubberDuck()
	rd.info()
	rd.quack()
	rd.fly()
	print('*'*10)