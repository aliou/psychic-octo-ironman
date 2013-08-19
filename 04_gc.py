def string_sum(a, b):
  return a + b

strings = open("files/rosalind_gc.txt").read().split('>')
del strings[0]

gc = {}
for item in strings:
  string_l = item.split()
  del string_l[0]
  string = reduce(string_sum, string_l, "")
  gc[item.split()[0]] = (string.count('G') + string.count('C')) * 100.0 / len(string)

keys = gc.keys()
values = gc.values()
print "%s\n%s" % (keys[values.index(max(values))], max(values))
