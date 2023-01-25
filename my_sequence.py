#### USING ONLY Python's STANDARD LIBRARY COMPLETE THE FOLLOWING CODE

#### There are 5 methods worth 25 points that you must write to gain 
#### full credit for the my_sequence.py module: the reset methods 
#### for the Arithmetic and Geometric Classes, as well as, the asList 
#### methods for the Arithmetic, Geometric, and Quadratic Classes


import math


import math

# An arithmetic sequence, is a sequence of numbers such that the 
# difference between consecutive terms is constant. This constant is referred
# to as the common difference. Any arithmetic sequence can be defined as a 
# linear function of the form f(n) = a1 + (n-1)d, where a1 is the first term,
# d is the common difference, and the domain n is the natural numbers 
# {1,2,3,..} 
class Arithmetic:
	# initializer with default first_term = 1, default common_difference = 5
	# and default max_terms = 10
	def __init__(self, first_term = 1, common_difference = 5, max_terms = 10):
		self.first_term = first_term
		self.common_difference = common_difference
		self.max_terms = max_terms
	
	# ****** COMPLETE THE METHOD BELOW	
	# @param mx_plus_b a string containing a linear expression of the form 
	# mx + b  
	# Precondition: mx_plus_b must be a valid linear expression in the form
	# mx + b 
	# sets first_term and common_difference to the correct values based on
	# the parameter mx_plus_b, default max terms = 5
	def reset(self, mx_plus_b = 'x', max_terms = 5):
		self.max_terms = max_terms

		x_index = mx_plus_b.index("x")

		if len(mx_plus_b) == 1:
			m = int(1)
			self.first_term = m
			self.common_difference = m*2 - self.first_term
		elif len(mx_plus_b)==2 and "-" in mx_plus_b:
			m = int(-1)
			self.first_term = m
			self.common_difference = m*2 - self.first_term
		else:
			m = float(mx_plus_b[:x_index])
			if "+" in mx_plus_b:
				plus_index = mx_plus_b.index("+")
				b = float(mx_plus_b[plus_index+1:])
				self.first_term = m + b
				self.common_difference = (m*2 + b) - self.first_term
			else:
				self.first_term = m
				self.common_difference = m*2 - self.first_term
		
		# while x >= [max_terms]:
		# 	for i in self.max_terms:
		# 		x = self.first_term + self.common_difference
		# 		return x



		
		
	# ****** COMPLETE THE METHOD BELOW
	# returns the sequence as a list
	# @param none 
	# @return a list containing the terms of the sequence rounded to 
	# a precision of 6
	def asList(self):
		lyst = []
		for num in range(1, self.max_terms+1):
			value = self.first_term + (num-1) * self.common_difference
			value = round(value, 6)
			lyst.append(value) 
		return lyst



		
		
# A geometric sequence, is a sequence of numbers where each term after the
# first is found by multiplying the previous one by a fixed, non-zero number 
# called the common ratio. Any geometric sequence can be defined as an 
# exponential function of the form f(n) = a1(r)^n, where a1 is the first 
# term, r is the common ratio raised to the n power, and the domain n is 
# the whole numbers {0,1,2,3,..} 
class Geometric:
	# initializer with default first_term = 1, default common_ratio = 2
	# and default max_terms = 10
	def __init__(self, first_term = 1, common_ratio = 2, max_terms = 10):
		self.first_term = first_term
		self.common_ratio = common_ratio
		self.max_terms = max_terms
		
	# ****** COMPLETE THE METHOD BELOW	
	# @param arn a string containing an exponential expression of the form 
	# a(r)^n or r^n, r > 0, r not equal to 1, a not equal to 0  
	# Precondition: arn must be a valid exponential expression of the form
	# a(r)^n or r^n, r > 0, r not equal to 1, a not equal to 0   
	# sets first_term and common_ratio to the correct values based on
	# the parameter arn, default exponential expression = 2^n
	# default max terms = 5
	# @return void
	def reset(self, arn = '2^n', max_terms = 5):
		self.max_terms = max_terms
		if "(" in arn:
			left_paren = arn.index("(")
			right_paren = arn.index(")")
			r = float(arn[left_paren+1:right_paren]) 
			a = float(arn[:left_paren])
			self.first_term = a * (r)**0
			self.common_ratio = r
		else:
			exp_index = arn.index("^")
			if "-" in arn:
				minus_index = arn.index("-")
				r = int(arn[minus_index+1:exp_index])
				self.first_term = -r**0
			else:
				r = int(arn[:exp_index])
				self.first_term = r**0
				self.common_ratio = r
			
		
	# ****** COMPLETE THE METHOD BELOW	
	# returns the sequence as a list
	# @param none 
	# @return a list containing the terms of the sequence rounded to 
	# a precision of 6
	def asList(self):
		lyst = []
		for num in range(self.max_terms):
			value = self.first_term*(self.common_ratio)**num
			value = round(value, 6)

			lyst.append(value)
		return lyst
		
		
	
# A quadratic sequence, is a sequence of numbers in which the second 
# differences between each consecutive term differ by the same amount, 
# called a common second difference. Any geometric sequence can be defined 
# as a quadratic function of the form f(n) = An^2 + Bn + C, where A, B, and
# C are constants, and n^2 means n raised to the 2nd power.
class Quadratic:
	# initializer with default constants A = 1, B = 0, C = 0
	# and default max_terms = 10
	def __init__(self, A = 1, B = 0, C = 0, max_terms = 10):
		self.A = A
		self.B = B
		self.C = C
		self.max_terms = max_terms
		
	# ****** COMPLETE THE METHOD BELOW	
	# returns the sequence as a list
	# @param none 
	# @return a list containing the terms of the sequence
	def asList(self):
		lyst = []

		for num in range(1,self.max_terms+1):
			value = self.A*num**2 + self.B*num + self.C
			value = round(value, 6)
			lyst.append(value)

		return lyst