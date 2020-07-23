import abc

class Animal(abc.ABC):
	
	def __init__(self):
		pass

	@abc.abstractmethod
	def make_sound(self):
		pass


class Dog(Animal):

	def __init__(self):
		pass

	def make_sound(self):
		self.bark()

	def bark(self):
		print("Woof Woof!")


class Cat(Animal):

	def __init__(self):
		pass

	def make_sound(self):
		self.meow()

	def meow(self):
		print("Meowwwww!")


if __name__=='__main__':

	d = Dog()
	d.make_sound()

	c = Cat()
	c.make_sound()