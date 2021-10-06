class MyClass:
	def __init__(self):
		self.x=1 #public var
		self.__y=2 #private var
	def display(self):
		print(self.x) #x is available directly
		print(self._MyClass__y)	#name mangling required
print('Accessing variables through method:')
m=MyClass()
m.display()
print('Access variables through instance:')
print(m.x)
print(m._MyClass__y) #name mangling required