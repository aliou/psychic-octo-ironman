value = File.open("files/rosalind_perm.txt", "r").read
perms = (1..value.to_i).to_a.permutation
puts perms.count
perms.each {|p| puts p.to_s}
