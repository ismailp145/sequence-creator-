#### USING ONLY python's STANDARD LIBRARY COMPLETE THE FOLLOWING CODE

import my_sequence

# Create a default Arithmetic sequence object
A1 = my_sequence.Arithmetic()
# Create a default Geometric sequence object
G1 = my_sequence.Geometric()
# Create a default Quadratic sequence object
Q1 = my_sequence.Quadratic()
# Create a specific Quadratic sequence object
Q2 = my_sequence.Quadratic(1,1,1,5)

# test the asList method for all sequence objects
print(A1.asList())
print(G1.asList())
print(Q1.asList())
print(Q2.asList())

# test the reset method for the Arithmetic sequence object
A1.reset('1.1x+1')
print(A1.asList())

# test the reset method for the Geometric sequence object
G1.reset('5(2.1)^n')
print(G1.asList())





	
