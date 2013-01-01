chars = {"A" => 0, "C" => 0, "G" => 0, "T" => 0}

File.open("files/rosalind_dna.txt", 'r').each_char do |char|
    chars[char] += 1 unless char == "\n"
end

puts chars.values.join(' ')
