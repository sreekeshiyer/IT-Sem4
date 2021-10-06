from abc import * 
#an interface to connect to any database 
class MyClass(ABC): 
	@abstractmethod 
	def connect(self): 
		pass 
	@abstractmethod 
	def disconnect(self): 
		pass 
class MySQL(MyClass): 
	def connect(self): 
		print("Connected to MySQL database") 
	def disconnect(self): 
		print("Disconnected from MySQL database") 
class Oracle(MyClass): 
	def connect(self): 
		print("Connected to Oracle database") 
	def disconnect(self): 
		print("Disconnected from Oracle database") 
obj1 = MySQL() 
obj1.connect() 
obj1.disconnect() 
obj2 = Oracle() 
obj2.connect() 
obj2.disconnect() 