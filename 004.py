def diff_letters(s, t):
  return sum (s[i] != t[i] for i in range(len(s)))

a, b = open("files/rosalind_hamm.txt").read().split()

print "Hamming distance:", diff_letters(a, b)
