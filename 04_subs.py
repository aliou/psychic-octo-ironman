string, sub = open("files/rosalind_subs.txt").read().split()

idxs = []
i = string.find(sub)
while i >= 0:
  idxs.append(i + 1)
  i = string.find(sub, i + 1)

print idxs
