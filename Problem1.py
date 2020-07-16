# PROBLEMS FROM HACKEREARTH
# PROBLEMS FOR PRACTICE

# PROBLEM 1 JADOO AND KOBA

# Jadoo, the space alien has challenged Koba to a friendly duel.
# He asks Koba to write a program to print out all numbers from 70 to 80.
# Knowing perfectly well how easy the problem is, the Jadoo adds his own twist to the challenge.
# He asks Koba to write the program without using a single number in his program
# and also restricts the character limit to 100.

# Solution

for number in range(69, 80):
    number = number + 1
    print(number)

# write a program to convert weight into kg

weight = int(input("Please write down weight here: "))  # please put the weight in lbs
convert_kg = weight * 0.45
print(convert_kg)

course = "Python's course for beigneers "
print(course)

name = "tom"
name1 = "jerry "

message = name + ' [' + name1 + '] is a cioder'
msg = f'{name} + {[ name1]}is a coder '
print(msg)
print(message)
