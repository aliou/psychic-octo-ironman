from misc.codon import codon_table

s = open("files/rosalind_prot.txt").read()

i = 0
prot = ""
while i < range(len(s)):
  codon = s[i:i + 3]
  if codon != "\n" and codon_table[codon] != "Stop":
    prot += codon_table[codon]
  else:
    break
  i += 3

print prot
