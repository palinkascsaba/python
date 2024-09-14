import random
from collections import Counter
def sequence_randomizer(length,is_dna=True):
    if is_dna:
        nucleotides = ("ACTG")
    else:
        nucleotides = ("ACUG")
    sequence =''
    for x in range(length):
        sequence += random.choice(nucleotides)
    print (sequence)
    return sequence    

#DNS komplement szál készítő
def komplementator(sequence, is_dna=True):
    komplement = ''
    for nucleotide in sequence: 
        if is_dna:
            if nucleotide == "A":
                komplement_bazis = "T"
            elif nucleotide == "T":
                komplement_bazis = "A"
            elif nucleotide == "G":
                komplement_bazis = "C"
            elif nucleotide == "C":
                komplement_bazis = "G"       
        else:
            if nucleotide == "A":
                komplement_bazis = "U"
            elif nucleotide == "U":
                komplement_bazis = "A"
            elif nucleotide == "G":
                komplement_bazis = "C"
            elif nucleotide == "C":
                komplement_bazis = "G"
        komplement += komplement_bazis
    print (f'\nThe original strand is \n{sequence} \nThe complementary strand is: \n{komplement}')
    return komplement

sequence = sequence_randomizer(100,is_dna=True)

komplementator(sequence, is_dna=True)

nucleotide_count = Counter(sequence)
print ('\nThe numbers of nucleotides are:')
for nucleotide, count in nucleotide_count.items():
    print(f'{nucleotide}: {count}')

print("\nNucleotide percentages:")
for nucleotide, count in nucleotide_count.items():
    percentage = (count / len(sequence)) * 100
    print(f"{nucleotide}: {percentage:.0f}%")
