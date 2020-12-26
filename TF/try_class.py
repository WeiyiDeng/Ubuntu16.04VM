class car:
	def __init__(self,col,mil):
		self.color = col
		self.millage = mil
	def myfunc(self):
		return "The {} car has {} miles".format(self.color,self.millage)
	def __str__(self):
		return "This is a {} miles {} car".format(self.color,self.millage)
		
c1 = car("red",10000)
c2 = car("blue",80000)

c1.myfunc()
print(c2)
print(c1.myfunc())

# f"This is a {self.millage} miles {self.color} car"
