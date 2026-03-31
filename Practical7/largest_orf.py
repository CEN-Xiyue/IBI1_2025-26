# identify the largest ORF	that can be generated from this sequence
# report	the	length	of	that	ORF	in	nucleotides
import re
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start = 'AUG'
stop = ['UAA','UAG','UGA']
# initialize
maxlength = 0
maxseq = ""
length = 0
# if read the start codon, start counting the length
for i in range(len(seq)-2):
    codon  = seq[i:i+3]
    if codon == start:
        for j in range(i,len(seq)-2,3):
            currentcodon = seq[j:j+3]
            if currentcodon in stop:
                length = j - i
                if length > maxlength:
                    maxlength = length
                    maxseq = seq[i:j]
                break
print("The largest ORF is:",maxseq)
print("The length is:",maxlength)
