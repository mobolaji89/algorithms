# A few possible Ruby Solutions


# Solution 1 - zip method

def finder(arr1, arr2)

  # Sort the arrays
  arr1.sort!
  arr2.sort!

  # zip both arrays and compare
  arr1.zip(arr2) do |a, b|
    return a if b == nil
  end

end

# # Solution 2 - array subtraction method

def finder(a,b)

  c = a.sort - b.sort
  return c.first # c[0]

end

# Solution 3 - for in loop with .include?

def finder(arr1, arr2)

  for num in arr1 do
    return num if !arr2.include?(num)
  end

end

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
