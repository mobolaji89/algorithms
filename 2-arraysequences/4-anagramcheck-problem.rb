# Ruby Solutions

# Solution 1 - simpler approach

def anagram(s1,s2)
  # Remove spaces and lowercase letters
  s1 = s1.downcase.delete(' ') # could also use gsub with regex as alternative
  s2 = s2.downcase.delete(' ')

  # sort string alphabetically
  s1 = s1.split('').sort.join()
  s2 = s2.split('').sort.join()

  return s1 == s2

end


# Solution 2 - more optimal, manual interview approach

def anagram2(s1, s2)
  # Remove spaces and lowercase letters
  s1 = s1.downcase.delete(' ')
  s2 = s2.downcase.delete(' ')

  # Edge Case to check if same number of letters
  return false if s1.length != s2.length

  # Create a counting hash
  count = {}

  # Fill hash for first string (add counts)
  s1.each_char do |letter|
    if count.include?(letter)
      count[letter] += 1
    else
      count[letter] = 1
    end
  end

  # Fill hash for second string (subtract counts)
  s2.each_char do |letter|
    if count.include?(letter)
      count[letter] -= 1
    else
      count[letter] = 1
    end
  end

  # Check that all counts are 0
  count.each_key do |key|
    return false if count[key] != 0
  end

  # Otherwise they are anagrams
  return true

end

anagram("Do g", "god") # true
anagram("Public relations", "crap built on lies") # true
anagram("public relations", "crap bufgffh ilt on lieds") # false
anagram("clint eastwood", "old west action") # true

anagram2("Do g", "god") # true
anagram2("Public relations", "crap built on lies") # true
anagram2("public relations", "crap bufgffh ilt on lieds") # false
anagram2("clint eastwood", "old west action") # true
