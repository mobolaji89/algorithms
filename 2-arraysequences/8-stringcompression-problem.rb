def compress(str)
  output = ''
  len = str.length

  # Edge case - Check for length 0
  return '' if len == 0

  # Edge case - Check for length 1
  return str + '1' if len == 1

  # Initialize count and index variables
  count = 1
  i = 1

  while i < len do
    if str[i] == str[i-1]
      count += 1
    else
      output = output + str[i-1] + count.to_s
      count = 1 #reset count
    end
    i += 1
  end

  output = output + str[i-1] + count.to_s

  return output
end

p compress('AAAAABBBBCCCC')
p compress('')
p compress('A')
