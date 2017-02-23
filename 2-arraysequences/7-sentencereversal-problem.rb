# Solution 1 - Simple approach
def rev_word(str)
  str.split(' ').reverse.join(' ')
end


#Solution 2 - More manual interview approach

def rev_word2(str)
  words = []
  len = str.length
  space = ' '

  # index tracker
  i = 0

  # while we haven't iterated through the entire string
  while i < len do

    # if current letter is not a space then we know a word starts at that index
    if str[i] != space
      word_start = i

      # keep going until we haven't hit another space
      while i < len && str[i] != space
        # Get index where word ends
        i += 1
      end

      # once while loop has completed push to words array
      words.push(str[word_start...i])

    end

    # add to index tracker
    i += 1
  end

  #Join the reversed words array
  return words.reverse.join(' ')

end

p rev_word('This is the best')
p rev_word('   Hello John    how are you   ')
