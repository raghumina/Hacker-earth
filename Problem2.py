# PROBLEM 2

# Jadoo and DNA Transcription
# PROBLEM

# Jadoo, the Space Alien has befriended Koba upon landing on Earth.
# Since then, he wishes Koba to be more like him.
# In order to do so he decides to slowly transcribe Koba's DNA into RNA.
# But he has to write a very short code in order to do the transcription so as not to make Koba aware of the change.
# The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).
# The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).
# Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
# G --> C
# C --> G
# T --> A
# A --> U
# Input: The input will always be a string of characters.
# Output: The output should always be a string of characters. In the case of invalid input,
# you should output Invalid Input as a string.

# Solution
'''
varaibles = str.upper(input())
if varaibles == "G":
 print(varaibles.replace('G','C'))
elif varaibles == "C":
 print(varaibles.replace("C","G"))
elif varaibles == "T":
 print(varaibles.replace("T","A"))
elif varaibles == "A":
 print(varaibles.replace("A","T"))
'''

# LETS TRY ANOTHER WAY TO SOLVE THIS PROBLEM

def vairable(input):
 if input == "G" or "C" or "T" or "A":
  print(input.replace("G","C"))



