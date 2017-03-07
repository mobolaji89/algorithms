# Reverse a string

def reverse(str)
  return str if str.length <= 1 #base case
  return reverse(str[1..str.length]) + str[0]
end

reverse('hello world')
