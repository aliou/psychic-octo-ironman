from misc.codon import codon_table

strings = open("files/rosalind_splc.txt").read().split('>')
del strings[0]

strings = [string.split()[1] for string in strings]
dna = strings[0]
del strings[0]

for item in strings:
  dna = dna.replace(item, "")

dna = dna.replace("T", "U")

i = 0
prot = ""
while i < range(len(dna)):
  codon = dna[i:i+3]
  if codon != "" and codon_table[codon] != "Stop":
    prot += codon_table[codon]
  else:
    break
  i += 3

print prot
