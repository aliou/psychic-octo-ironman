corres = {"A" => "T", "C" => "G", "G" => "C", "T" => "A"}

dna_string = File.read("files/rosalind_revc.txt").chop!.reverse!
reversed_string = ""

dna_string.each_char do |char|
  reversed_string += corres[char]
end

puts reversed_string
