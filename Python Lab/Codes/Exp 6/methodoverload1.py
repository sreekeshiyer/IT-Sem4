class MyClass: 
	def sum(self, a=None, b=None, c=None): 
		if a!=None and b!=None and c!=None: 
			print(a+b+c) 
		elif a!=None and b!=None:
			print(a+b) 
		else: 
              		print("Enter atleast 2 arguments") 
obj = MyClass() 
obj.sum(1,2,3) 
obj.sum(1,2) 
obj.sum(1) 