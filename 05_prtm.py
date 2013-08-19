from misc.protein import protein_weight

protein = open("files/rosalind_prtm.txt").read().split()[0]
weight = sum(protein_weight[protein[i]] for i in range(len(protein)))

print weight
