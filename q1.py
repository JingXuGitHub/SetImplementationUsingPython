# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 19:15:27 2018

@author: Administrator
"""

class Set(object):

	def __init__(self, lt):
		self.__setlist = []
		self.id = 0
		self.extend(lt)
	
	def __iter__(self):
		return self
		
	def __next__(self):
		self.id += 1
		try:
			return self.__setlist[self.id -1]
		except IndexError:
			self.id = 0
			raise StopIteration
	
	def extend(self, lt):
		"""Add several items at once."""
		for i in lt:
			self.addElement(i)
		return self
            
	def addElement(self, item):
		"""Add one item to the set."""
		if item in self.__setlist:
			pass
		else:
			self.__setlist.append(item)
		return self
		
	def removeElement(self, item):
		"""Remove an item from the set."""
		if self.contains(item):
			self.__setlist.remove(item)
		else:
			return False
		return self
	
	def clear(self):
		"""Remove all elements from the set."""
		while self.len() != 0:
			self.__setlist.pop()
		return True
		
	def len(self):
		"""Give the item numbers of the set."""
		return len(self.__setlist)

	def contains(self, item):
		"""Check whether the set contains a certain item."""
		return item in self.__setlist
        
	def union(self, s):
		result = Set([])
		for i in self:
			result.addElement(i)
		for i in s:
			result.addElement(i)
		return result
		
	def intersection(self, s):
		result = Set([])
		for i in self:
			if s.contains(i):
				result.addElement(i)
		return result
		
	def difference(self, s):
		result = Set([])
		for i in self:
			result.addElement(i)
		for i in s:
			if result.contains(i):
				result.removeElement(i)
		return result
	
	def cartesionProduct(self, s):
		result = Set([])
		if s.len() != 0 and self.len() != 0:
			for i in self:
				for j in s:
					ele = (i,j)
					result.addElement(ele)
		else:
			return False
		return result
		
	def isSubset(self, s):
		for ele in s:
			if ele in self.__setlist:
				pass
			else:
				return False
		return True
		
	def isEmpty(self):
		if self.len() == 0:
			return True
		else:
			return False
	
	def isElement(self, item):
		return self.contains(item)
		
	def isEqual(self, s):
		return self.isSubset(s) and s.len() == self.len()
		
	def getCardinality(self):
		return self.len()
  
	def toArray(self):
		result = []
		for i in self:
			result.append(i)
		return result
		
	def printSet(self):
		if self.len() == 0:
			print("There is no elements in the set!")
		else:
			print('{', sep=' ', end='')
			for i in range(self.len()-1):
				print(self.__setlist[i], sep=' ', end=', ')
			print(self.__setlist[self.len()-1], '}', sep='')
		      
"""Test"""
testset1 = Set([])
testset2 = Set([])
result = Set([])
s = 0
str1 = input("Input the set elements: ")
if len(str1) != 0:
	str2 = str1.split(" ")
	for i in str2:
		testset1.addElement(i)
	print('The set you input is: ', end='')
	testset1.printSet()
	print('')
else:
	print('The set you input is EMPTY!')
menulist = ['Enter: ',
		'1  for union', 
		'2  for intersection', 
		'3  for difference', 
		'4  for Cartesian product', 
		'5  for subset', 
		'6  for isEqual', 
		'7  for isEmpty', 
		'8  for isElement', 
		'9  for getCardinality', 
		'10 for addElement', 
		'11 for removeElement', 
		'12 for clear', 
		'13 for toArray', 
		'14 for print',
		'15 for set initialization']
def menu():
	for i in range(1, len(menulist)):
		print(menulist[i])
	return int(input())
s = menu()
while s in range(1,16):
	while s in range(1,7):
		str2 = input("Please input another set elements: ")
		str2 = str2.split(" ")
		testset2 = Set(str2)
		if s == 1:
			result = testset1.union(testset2)
			if result.len() != 0:
				print("The union set is: ")
				result.printSet()
			else:
				print("The union set is empty!")
		if s == 2:
			result = testset1.intersection(testset2)
			if result.len() != 0:
				print("The intersection set is: ")
				result.printSet()
			else:
				print("The intersection set is empty!")
		if s == 3:
			result = testset1.difference(testset2)
			if result.len() != 0:
				print("The difference set is: ")
				result.printSet()
			else:
				print("The difference set is empty!")
		if s == 4:
			result = testset1.cartesionProduct(testset2)
			if result != False:
				print("The cartesionProduct set is: ")
				result.printSet()
			else:
				print("The cartesionProduct set is empty!")
		if s == 5:
			if testset1.isSubset(testset2):
				print("The second set is a subset of the first set")
			else:
				print("The second set is NOT a subset of the first set")
		if s == 6:
			if testset1.isEqual(testset2):
				print("The second set is euqal to the first set")
			else:
				print("The second set is NOT euqal to the first set")
		s = menu()		
	while s in range(7,15):
		if s == 7:
			if testset1.isEmpty():
				print("The set is EMPTY!")
			else:
				print("The set is NOT EMPTY!")
		if s == 8:
			str = input("Please input an item to check if it's in the set: ")
			if testset1.isElement(str):
				print("The item is an element of the set!")
			else:
				print("The item is NOT an element of the set!")
		if s == 9:
			print("The cardinality of the set is: ", testset1.getCardinality())
		if s == 10:
			str = input("Please input the element you want to add: ")
			result = testset1.addElement(str)
			print("The new set is: ")
			result.printSet()
		if s == 11:
			str = input("Please input the item you want to remove: ")
			result = testset1.removeElement(str)
			if result == False:
				print("The item is not in the set!")
			else:
				print("The set after remove is: ")
				result.printSet()
		if s == 12:
			if testset1.clear():
				print("All the element in the set have been cleared!")
		if s == 13:
			print("The set was converted to a one dimenional array: ", testset1.toArray())
		if s == 14:
			print("The set is: ")
			testset1.printSet()
		s = menu()
	if s == 15:
		testset1.clear()
		str1 = input("Initialization, please input the NEW set elements: ")
		for i in str1:
			testset1.addElement(i)
		print('The NEW set you input is: ', end='')
		testset1.printSet()
		print('')
		s = menu()
