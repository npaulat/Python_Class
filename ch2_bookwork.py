print("Question 2.1")		# Print the question number
print('-----------------') 	# table heading
F = 0	 			# start value for C
dF = 10 			# increment of C in loop
print("{0:<5} {1:<5}".format("F","C"))			# Print column headers so I know what the hell is going on
while F <= 100: 		# loop heading with condition
	C = (F-32)*(5/9)	# 1st statement inside loop
	print("{0:<5} {1:<5}".format(F,round(C,2))) 		# 2nd statement inside loop
	F = F + dF 		# 3rd statement inside loop
print('------------------') 	# end of table line (after loop)
print("Question 2.10")
print("-------------------")
print("Simulate operations on lists by hand")

#Creates a list named "a"
a = [1, 3, 5, 7, 11]

#Creates a list named "b"
b = [13, 17]

#Concatenates list b to list a to create a new list "c"
c = a + b

#Sanity check to make sure "c" prints the way you want it to
print c

#replaces the first value (13) in list b with the value (-1)
b[0] = -1

#creates a new list named "d"... basically adding 1 to every value in list a
d = [e+1 for e in a]

#prints list d
print d

#appends a zero on to the end of list d
d.append(b[0] + 1)

#appends an 18 onto the end of list d
d.append(b[-1] + 1)

#prints the last two values in the list
print d[-2:]

#for every value in list a
for e1 in a:

	#as well as every value in list b
	for e2 in b:

		#print the sum of each corresponding value between the two lists
		print e1 + e2

#0
#18
#2
#20
#4
#22
#6
#24
#10
#28
print("Question 2.11")
print("-------------------")
print("Compute a mathematical sum")

s = 0
k = 1
M = 100

for k in range(1, M+1):
	s += 1/k

print(s)
print("Question 2.12")
print("-------------------")
print("Compute a mathematical sum")

s = 0
k = 1
M = 100

while k <= M:
	s += 1/k
	k += 1

print(s)
print("Question 2.13")
print("-------------------")
print("Simulate a program by hand. Calculating interest return.")

initial_amount = 100
p = 5.5 		# interest rate
amount = initial_amount
years = 0
while amount <= 1.5*initial_amount:
	amount += amount + p/100*amount
	years += years + 1
	print(years,amount)



#Part A
#Year	Amount
#1 	105.5
#2 	111.3025
#3 	117.4241375
#4 	123.8824650625
#5 	130.6960006409375
#6 	137.88428067618906
#7 	145.46791611337946
#8	153.46865149961533

#Part B
#Because Python 2 sucked at dividing ints

#Part C
#See Above

#Part D
#Calculates the amount of years it would take to get to roughly 1.5 times the initial amount invested via compounding interest.
print("Question 2.14")
print("-------------------")
print("Explore Python documentation.")

import math
math.asin()
print("Question 2.15")
print("-------------------")
print("Index a nested list")

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

#PART A
#1
q[0][0]

#2
q[1]

#3
q[-1][-1]

#4
q[1][0]

#5
[-1] references the last list within the list
[-2] references the second to the last value in the last list


#PART B
i = each list within q
j = each value within each individual list
print("Question 2.16")
print("-------------------")
print("Store data in lists")

#Generate lists
FAH=[]
CEL=[]
APX=[]

F = 0                           # start value for C
dF = 10                         # increment of C in loop
print("{0:<5} {1:<8} {2:<5}".format("F", "C", "C Approximate")) # Print column headers so I know what the hell is going on


while F <= 100:
	C = (F-32)*(5/9)
	CA = int(round(C/5)*5)
	CEL.append(C)
	APX.append(CA)
	FAH.append(F)
#	print("{0:<5} {1:<8} {2:<5}".format(F, round(C,2), CA))
	F = F + dF

conversion = [[F, C, CA]
	for F, C, CA in zip(FAH, CEL, APX)]

for F, C, CA, in conversion:
	print("{0:<5} {1:<8} {2:<5}".format(F, round(C,2), CA))


print('-------------------------------')        # end of table line (after loop)
print("Question 2.17")
print("-------------------")
print("Store data in a nested list")

Vo = 50         #Initial Velocity. For some reason this doesn't work at zero?
g = 9.81                #Force of gravity in meters per second
start = 0               #Initiate
stop = int(2*Vo/g)      #Finish


T=[]
Y=[]

for t in range (start,stop):
        y = (Vo*t)-(.5*g*t**2)
        T.append(t)
        Y.append(y)

#print("{0:<5}{1:<5}".format("t","y"))

#for t,y in zip(T,Y):
#        print("{0:<5}{1:<5}".format(t,y))


#print(T)
#print(Y)

print("--------------------")
print("PART A")

ty1 = [T,Y]
print(ty1)

for i in range(len(T)):
	print(round(ty1[0][i],2), round(ty1[1][i],2))


print("------------------------------")
print("PART B")

ty2 = [[t,y] for t,y in zip(T,Y)]

print(ty2)

for t,y in ty2:
	print(t,round(y,2))
print("Question 2.18")
print("-------------------")
print("Values of boolean expressions")

C = 41			# C now represents the value 41
C == 40			# F, C=41
C != 40 and C < 41	# F, C=41... so it's not less than
C != 40 or C < 41	# T, the "or" allows for the first condition to be met
not C == 40		# T, C=41
not C > 40		# F, C is > 40
C <= 41			# T, C is equal to 41
not False		# T
True and False		# F... get that dialetheia BS outta here
False or True		# T, can be either, but not both. 
False or False or False	# lol... F
True and True and False	# T
False == 0		# T
True == 0		# F
True == 1		# T

print("Question 2.19")
print("Explore round-off errors from a large number of inverse operations")
print("-------------------")

from math import sqrt
for n in range(1, 60):
	r = 2.0
	for i in range(n):
		r = sqrt(r)
	for i in range(n):
		r = r**2
	print('%d times sqrt and **2: %.16f' % (n, r))



##############################
#	1 times sqrt and **2: 2.0000000000000004
#	2 times sqrt and **2: 1.9999999999999996
#	3 times sqrt and **2: 1.9999999999999996
#	...
#	51 times sqrt and **2: 1.6487212645509468
#	52 times sqrt and **2: 1.0000000000000000
#	53 times sqrt and **2: 1.0000000000000000


# It has to do with the accuracy of the python float.
# Once we hit numbers greater than 52 the float accuracy falls off and we get the appropriate result of 1. 

print("Question 2.2")		# Print the question number
print('-------------------------------') 	# table heading
F = 0	 			# start value for C
dF = 10 			# increment of C in loop
print("{0:<5} {1:<8} {2:<5}".format("F", "C", "C Approximate"))	# Print column headers so I know what the hell is going on
while F <= 100: 		# loop heading with condition
	C = (F-32)*(5/9)	# 1st statement inside loop
	CA = int(round(C/5)*5)	# Round to the nearest 5th degree
	print("{0:<5} {1:<8} {2:<5}".format(F, round(C,2), CA)) 	# 2nd statement inside loop
	F = F + dF 		# 3rd statement inside loop
print('-------------------------------') 	# end of table line (after loop)
print("Question 2.20")
print("Explore what zero can be on a computer")
print("-------------------")

eps = 1.0				# eps = 1
while 1.0 != 1.0 + eps:			# while 1 does not equal 1 + eps
	print("..........", eps)	# print dots and eps
	eps = eps/2.0			# eps = eps/2
print("final eps:", eps)		# print

# Machine epsilon. It's another problem with floating point arithmetic in computers.
print("Question 2.21")
print("Compare two real numbers with a tolerance")
print("-------------------")

a = 1 / 947.0 * 947
b = 1
if a != b:
    print("Wrong result!")

print("--------------------")

a = 1 / 947.0 * 947
b = 1
if abs(a - b) > 1e-10000000000000:
    print("Wrong result!")
print("Question 2.22")
print("Interpret a code")
print("-------------------")

import time
t0 = time.time()
while time.time() - t0 > 10:
    print('....I like while loops!')
    # time.sleep(2)
print('Oh, no - the loop is over.')

#1. 17366638 times
#2. 0 times
print("Question 2.23")
print("Explore problems with inaccurate indentation")
print("-------------------")

C = -60; dC = 2
while C <= 60:
	F = (9.0/5)*C + 32
	print(C, F)
	C = C + dC


# I can't copy over the exact text from the book into my terminal, 
# but it looks like there's something wrong with the indentation pattern. So that's the first problem.
# Once fixed, you get a repeating sequence:
#
# -60 -76.0
# -60 -76.0
# -60 -76.0
# -60 -76.0
# -60 -76.0
#
#This is due to the fact that the last line needs to be included in the loop.
print("Question 2.24")
print("Investigate a for loop over a changing list")
print("-------------------")

x = 1	# X now equals 1
x = 1.	# X now equals 1.0
x = 1;	# x now equals 1
x = 1!	# error
x = 1?	# error
x = 1:	# error
x = 1,	# x now equals (1,)
print("Question 2.25")
print("Investigate a for loop over a changing list")
print("-------------------")

>>> numbers = range(10)
>>> print(numbers)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> for n in numbers:
... i = len(numbers)/2
... del numbers[i]
... print('n=%d, del %d' % (n,i), numbers)
...
n=0, del 5 [0, 1, 2, 3, 4, 6, 7, 8, 9]
n=1, del 4 [0, 1, 2, 3, 6, 7, 8, 9]
n=2, del 4 [0, 1, 2, 3, 7, 8, 9]
n=3, del 3 [0, 1, 2, 7, 8, 9]
n=8, del 3 [0, 1, 2, 8, 9]

#you're deleting the middle most number from the list in every iteration of the loop.
print("Question 2.3")
print("-----------------------")
print("Prime numbers up to 13")
primes = [2, 3, 5, 7, 11, 13]
for num in primes:
	print(num)
print("\n")

#Now adding the number 17 to the list
p = 17
primes.append(p)

#Print new title
print("Prime numbers up to 17")

for num in primes:
	print(num)
print("Question 2.4")
print("-------------------")
print("Print a run of odd numbers to a definied n")

n = 20 #The top end
i = 0 #initiate number sequence at zero

while i < int(round(n/2)):
	print(2*i+1)
	i+=1

print("Question 2.5")
print("-------------------")
print("Print the sum of all numbers up to, and including, a specified n")

n = 9
print(sum(range(n+1)))
print("Question 2.6")
print("-------------------")
print("PART A")
print("Calculate and print the energy level for n")
print("\n")

#Set up constants
EM = 9.1094e-31		#electron mass of hydrogen
EC = 1.6022e-19		#elementary charge
EPoV = 8.8542e-12	#elecrical permittiivity of a vacuum... probably did this one wrong
H = 6.6261e-34		#jouls?
# EL = Energy level... this is what we're trying to calculate
N = 1 			# the stage of an energy level. 
# fuck me

# It should look something like this??? Maybe?
# EL = -(EM*EC**4)/(8*EPoV**2*H**2)/(N**2)


print("{0:<5} {1:<5}".format("Level", "Energy"))
while N<=20:
	EL = -(EM*EC**4)/(8*EPoV**2*H**2)/(N**2)
	print("{0:<5} {1:<5}".format(N, EL))
	N = N+1

print("\n")
print("-------------------")
print("PART B")
print("Calculate and print the energy released as hydrogen moves in between levels")
print("\n")

Ni=1
Nf=5
# DeltaE = the energy emmittance as the atom changes levels. 

print("{0:<5} {1:<5}".format("Level", "Energy Released"))

while Ni <= Nf:
	DeltaE = -(EM*EC**4)/(8*EPoV**2*H**2)*((1/Ni**2)-(1/Nf**2))
	print("{0:<5} {1:<5}".format(Ni, DeltaE))
	Ni=Ni+1
print("Question 2.7")
print("-------------------")
print("PART A")
print("Generate a list of equally spaced x-coordinates using a for loop")

list = []
i = 0

for i in range(0,10):
        coords = tuple([i+1,0])
        list.append(coords)
        i+=1
print(list)


print("\n")
print("PART B")
print("Generate a list of equally spaced x-coordinates using a list comprehension")
print("\n")

list_comp = [tuple([i+1,0]) for i in range(0,10)]
print(list_comp)
print("Question 2.8")
print("-------------------")
print("PART A")
print("Use a for loop to produce the table of falling velocity")

Vo = 50		#Initial Velocity. For some reason this doesn't work at zero? 
g = 9.81		#Force of gravity in meters per second
start = 0		#Initiate
stop = int(2*Vo/g)	#Finish

print("{0:<5}{1:<5}".format("t","y"))
for t in range (start,stop):
	y = (Vo*t)-(.5*g*t**2)
	print("{0:<5}{1:<5}".format(t,y))

#Pretty sure I did this incorrectly. But the question isn't worded that well.

print("Question 2.9")
print("-------------------")
print("PART A")
print("Use a for loop to produce the table of falling velocity")

Vo = 50		#Initial Velocity. For some reason this doesn't work at zero? 
g = 9.81		#Force of gravity in meters per second
start = 0		#Initiate
stop = int(2*Vo/g)	#Finish

print("{0:<5}{1:<5}".format("t","y"))

T=[]
Y=[]

for t in range (start,stop):
	y = (Vo*t)-(.5*g*t**2)
	T.append(t)
	Y.append(y)

for t,y in zip(T,Y):
	print("{0:<5}{1:<5}".format(t,y))

#Pretty sure I did this incorrectly, at least from a physics perspective.

print("Question 2.1")		# Print the question number
print('-----------------') 	# table heading
F = 0	 			# start value for C
dF = 10 			# increment of C in loop
print("{0:<5} {1:<5}".format("F","C"))			# Print column headers so I know what the hell is going on
while F <= 100: 		# loop heading with condition
	C = (F-32)*(5/9)	# 1st statement inside loop
	print("{0:<5} {1:<5}".format(F,round(C,2))) 		# 2nd statement inside loop
	F = F + dF 		# 3rd statement inside loop
print('------------------') 	# end of table line (after loop)
print("Question 2.10")
print("-------------------")
print("Simulate operations on lists by hand")

#Creates a list named "a"
a = [1, 3, 5, 7, 11]

#Creates a list named "b"
b = [13, 17]

#Concatenates list b to list a to create a new list "c"
c = a + b

#Sanity check to make sure "c" prints the way you want it to
print c

#replaces the first value (13) in list b with the value (-1)
b[0] = -1

#creates a new list named "d"... basically adding 1 to every value in list a
d = [e+1 for e in a]

#prints list d
print d

#appends a zero on to the end of list d
d.append(b[0] + 1)

#appends an 18 onto the end of list d
d.append(b[-1] + 1)

#prints the last two values in the list
print d[-2:]

#for every value in list a
for e1 in a:

	#as well as every value in list b
	for e2 in b:

		#print the sum of each corresponding value between the two lists
		print e1 + e2

#0
#18
#2
#20
#4
#22
#6
#24
#10
#28
print("Question 2.11")
print("-------------------")
print("Compute a mathematical sum")

s = 0
k = 1
M = 100

for k in range(1, M+1):
	s += 1/k

print(s)
print("Question 2.12")
print("-------------------")
print("Compute a mathematical sum")

s = 0
k = 1
M = 100

while k <= M:
	s += 1/k
	k += 1

print(s)
print("Question 2.13")
print("-------------------")
print("Simulate a program by hand. Calculating interest return.")

initial_amount = 100
p = 5.5 		# interest rate
amount = initial_amount
years = 0
while amount <= 1.5*initial_amount:
	amount += amount + p/100*amount
	years += years + 1
	print(years,amount)



#Part A
#Year	Amount
#1 	105.5
#2 	111.3025
#3 	117.4241375
#4 	123.8824650625
#5 	130.6960006409375
#6 	137.88428067618906
#7 	145.46791611337946
#8	153.46865149961533

#Part B
#Because Python 2 sucked at dividing ints

#Part C
#See Above

#Part D
#Calculates the amount of years it would take to get to roughly 1.5 times the initial amount invested via compounding interest.
print("Question 2.14")
print("-------------------")
print("Explore Python documentation.")

import math
math.asin()
print("Question 2.15")
print("-------------------")
print("Index a nested list")

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

#PART A
#1
q[0][0]

#2
q[1]

#3
q[-1][-1]

#4
q[1][0]

#5
[-1] references the last list within the list
[-2] references the second to the last value in the last list


#PART B
i = each list within q
j = each value within each individual list
print("Question 2.16")
print("-------------------")
print("Store data in lists")

#Generate lists
FAH=[]
CEL=[]
APX=[]

F = 0                           # start value for C
dF = 10                         # increment of C in loop
print("{0:<5} {1:<8} {2:<5}".format("F", "C", "C Approximate")) # Print column headers so I know what the hell is going on


while F <= 100:
	C = (F-32)*(5/9)
	CA = int(round(C/5)*5)
	CEL.append(C)
	APX.append(CA)
	FAH.append(F)
#	print("{0:<5} {1:<8} {2:<5}".format(F, round(C,2), CA))
	F = F + dF

conversion = [[F, C, CA]
	for F, C, CA in zip(FAH, CEL, APX)]

for F, C, CA, in conversion:
	print("{0:<5} {1:<8} {2:<5}".format(F, round(C,2), CA))


print('-------------------------------')        # end of table line (after loop)
print("Question 2.17")
print("-------------------")
print("Store data in a nested list")

Vo = 50         #Initial Velocity. For some reason this doesn't work at zero?
g = 9.81                #Force of gravity in meters per second
start = 0               #Initiate
stop = int(2*Vo/g)      #Finish


T=[]
Y=[]

for t in range (start,stop):
        y = (Vo*t)-(.5*g*t**2)
        T.append(t)
        Y.append(y)

#print("{0:<5}{1:<5}".format("t","y"))

#for t,y in zip(T,Y):
#        print("{0:<5}{1:<5}".format(t,y))


#print(T)
#print(Y)

print("--------------------")
print("PART A")

ty1 = [T,Y]
print(ty1)

for i in range(len(T)):
	print(round(ty1[0][i],2), round(ty1[1][i],2))


print("------------------------------")
print("PART B")

ty2 = [[t,y] for t,y in zip(T,Y)]

print(ty2)

for t,y in ty2:
	print(t,round(y,2))
print("Question 2.18")
print("-------------------")
print("Values of boolean expressions")

C = 41			# C now represents the value 41
C == 40			# F, C=41
C != 40 and C < 41	# F, C=41... so it's not less than
C != 40 or C < 41	# T, the "or" allows for the first condition to be met
not C == 40		# T, C=41
not C > 40		# F, C is > 40
C <= 41			# T, C is equal to 41
not False		# T
True and False		# F... get that dialetheia BS outta here
False or True		# T, can be either, but not both. 
False or False or False	# lol... F
True and True and False	# T
False == 0		# T
True == 0		# F
True == 1		# T

print("Question 2.19")
print("Explore round-off errors from a large number of inverse operations")
print("-------------------")

from math import sqrt
for n in range(1, 60):
	r = 2.0
	for i in range(n):
		r = sqrt(r)
	for i in range(n):
		r = r**2
	print('%d times sqrt and **2: %.16f' % (n, r))



##############################
#	1 times sqrt and **2: 2.0000000000000004
#	2 times sqrt and **2: 1.9999999999999996
#	3 times sqrt and **2: 1.9999999999999996
#	...
#	51 times sqrt and **2: 1.6487212645509468
#	52 times sqrt and **2: 1.0000000000000000
#	53 times sqrt and **2: 1.0000000000000000


# It has to do with the accuracy of the python float.
# Once we hit numbers greater than 52 the float accuracy falls off and we get the appropriate result of 1. 

print("Question 2.2")		# Print the question number
print('-------------------------------') 	# table heading
F = 0	 			# start value for C
dF = 10 			# increment of C in loop
print("{0:<5} {1:<8} {2:<5}".format("F", "C", "C Approximate"))	# Print column headers so I know what the hell is going on
while F <= 100: 		# loop heading with condition
	C = (F-32)*(5/9)	# 1st statement inside loop
	CA = int(round(C/5)*5)	# Round to the nearest 5th degree
	print("{0:<5} {1:<8} {2:<5}".format(F, round(C,2), CA)) 	# 2nd statement inside loop
	F = F + dF 		# 3rd statement inside loop
print('-------------------------------') 	# end of table line (after loop)
print("Question 2.20")
print("Explore what zero can be on a computer")
print("-------------------")

eps = 1.0				# eps = 1
while 1.0 != 1.0 + eps:			# while 1 does not equal 1 + eps
	print("..........", eps)	# print dots and eps
	eps = eps/2.0			# eps = eps/2
print("final eps:", eps)		# print

# Machine epsilon. It's another problem with floating point arithmetic in computers.
print("Question 2.21")
print("Compare two real numbers with a tolerance")
print("-------------------")

a = 1 / 947.0 * 947
b = 1
if a != b:
    print("Wrong result!")

print("--------------------")

a = 1 / 947.0 * 947
b = 1
if abs(a - b) > 1e-10000000000000:
    print("Wrong result!")
print("Question 2.22")
print("Interpret a code")
print("-------------------")

import time
t0 = time.time()
while time.time() - t0 > 10:
    print('....I like while loops!')
    # time.sleep(2)
print('Oh, no - the loop is over.')

#1. 17366638 times
#2. 0 times
print("Question 2.23")
print("Explore problems with inaccurate indentation")
print("-------------------")

C = -60; dC = 2
while C <= 60:
	F = (9.0/5)*C + 32
	print(C, F)
	C = C + dC


# I can't copy over the exact text from the book into my terminal, 
# but it looks like there's something wrong with the indentation pattern. So that's the first problem.
# Once fixed, you get a repeating sequence:
#
# -60 -76.0
# -60 -76.0
# -60 -76.0
# -60 -76.0
# -60 -76.0
#
#This is due to the fact that the last line needs to be included in the loop.
print("Question 2.24")
print("Investigate a for loop over a changing list")
print("-------------------")

x = 1	# X now equals 1
x = 1.	# X now equals 1.0
x = 1;	# x now equals 1
x = 1!	# error
x = 1?	# error
x = 1:	# error
x = 1,	# x now equals (1,)
print("Question 2.25")
print("Investigate a for loop over a changing list")
print("-------------------")

>>> numbers = range(10)
>>> print(numbers)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> for n in numbers:
... i = len(numbers)/2
... del numbers[i]
... print('n=%d, del %d' % (n,i), numbers)
...
n=0, del 5 [0, 1, 2, 3, 4, 6, 7, 8, 9]
n=1, del 4 [0, 1, 2, 3, 6, 7, 8, 9]
n=2, del 4 [0, 1, 2, 3, 7, 8, 9]
n=3, del 3 [0, 1, 2, 7, 8, 9]
n=8, del 3 [0, 1, 2, 8, 9]

#you're deleting the middle most number from the list in every iteration of the loop.
print("Question 2.3")
print("-----------------------")
print("Prime numbers up to 13")
primes = [2, 3, 5, 7, 11, 13]
for num in primes:
	print(num)
print("\n")

#Now adding the number 17 to the list
p = 17
primes.append(p)

#Print new title
print("Prime numbers up to 17")

for num in primes:
	print(num)
print("Question 2.4")
print("-------------------")
print("Print a run of odd numbers to a definied n")

n = 20 #The top end
i = 0 #initiate number sequence at zero

while i < int(round(n/2)):
	print(2*i+1)
	i+=1

print("Question 2.5")
print("-------------------")
print("Print the sum of all numbers up to, and including, a specified n")

n = 9
print(sum(range(n+1)))
print("Question 2.6")
print("-------------------")
print("PART A")
print("Calculate and print the energy level for n")
print("\n")

#Set up constants
EM = 9.1094e-31		#electron mass of hydrogen
EC = 1.6022e-19		#elementary charge
EPoV = 8.8542e-12	#elecrical permittiivity of a vacuum... probably did this one wrong
H = 6.6261e-34		#jouls?
# EL = Energy level... this is what we're trying to calculate
N = 1 			# the stage of an energy level. 
# fuck me

# It should look something like this??? Maybe?
# EL = -(EM*EC**4)/(8*EPoV**2*H**2)/(N**2)


print("{0:<5} {1:<5}".format("Level", "Energy"))
while N<=20:
	EL = -(EM*EC**4)/(8*EPoV**2*H**2)/(N**2)
	print("{0:<5} {1:<5}".format(N, EL))
	N = N+1

print("\n")
print("-------------------")
print("PART B")
print("Calculate and print the energy released as hydrogen moves in between levels")
print("\n")

Ni=1
Nf=5
# DeltaE = the energy emmittance as the atom changes levels. 

print("{0:<5} {1:<5}".format("Level", "Energy Released"))

while Ni <= Nf:
	DeltaE = -(EM*EC**4)/(8*EPoV**2*H**2)*((1/Ni**2)-(1/Nf**2))
	print("{0:<5} {1:<5}".format(Ni, DeltaE))
	Ni=Ni+1
print("Question 2.7")
print("-------------------")
print("PART A")
print("Generate a list of equally spaced x-coordinates using a for loop")

list = []
i = 0

for i in range(0,10):
        coords = tuple([i+1,0])
        list.append(coords)
        i+=1
print(list)


print("\n")
print("PART B")
print("Generate a list of equally spaced x-coordinates using a list comprehension")
print("\n")

list_comp = [tuple([i+1,0]) for i in range(0,10)]
print(list_comp)
print("Question 2.8")
print("-------------------")
print("PART A")
print("Use a for loop to produce the table of falling velocity")

Vo = 50		#Initial Velocity. For some reason this doesn't work at zero? 
g = 9.81		#Force of gravity in meters per second
start = 0		#Initiate
stop = int(2*Vo/g)	#Finish

print("{0:<5}{1:<5}".format("t","y"))
for t in range (start,stop):
	y = (Vo*t)-(.5*g*t**2)
	print("{0:<5}{1:<5}".format(t,y))

#Pretty sure I did this incorrectly. But the question isn't worded that well.

print("Question 2.9")
print("-------------------")
print("PART A")
print("Use a for loop to produce the table of falling velocity")

Vo = 50		#Initial Velocity. For some reason this doesn't work at zero? 
g = 9.81		#Force of gravity in meters per second
start = 0		#Initiate
stop = int(2*Vo/g)	#Finish

print("{0:<5}{1:<5}".format("t","y"))

T=[]
Y=[]

for t in range (start,stop):
	y = (Vo*t)-(.5*g*t**2)
	T.append(t)
	Y.append(y)

for t,y in zip(T,Y):
	print("{0:<5}{1:<5}".format(t,y))

#Pretty sure I did this incorrectly, at least from a physics perspective.

