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

# 1
rna = ""
sequence = str.upper(input())
for i in sequence:
    if i == "G":
        rna = rna + i.replace("G", "C")
    elif i == "C":
        rna = rna + i.replace("C", "G")
    elif i == "T":
        rna = rna + i.replace("T", "A")
    elif i == "A":
        rna = rna + i.replace("A", "U")
print(rna)

'''

# 3
sequence  = str.upper(input("Please enter a sequence "))

if "G" and "C" and "T" and "A" in sequence:
  rna = sequence.replace("G","C")
  sequence = sequence.replace("C","G")
  print(sequence)
#  rna = sequence.replace("T","A")
 # rna = sequence.replace("A","U")


'''
