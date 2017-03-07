# Array Flatten

=begin
Problem:

You are given an array of mixed items:
array= [1,"Hello”,true,[2,3,4]]

Write a function that takes this array as an argument and flattens it.
The output should be a single array:
[1,"Hello",true,2,3,4]

Note the subarray.
Without using .flatten , of course!
=end


# My iterative approach
def flatten(arr)
  i = 0

  while i < arr.length do

    until arr[i].class != Array # could also use arr[i].is_a?(Array)
      j = 0

      while j < arr[i].length do
        arr.push(arr[i][j])
      j += 1
      end

      arr.delete(arr[i])
    end

    i+=1
  end

  return arr
end

# Recursive approach

def flatten(arr)
  flat_arr = []
  arr.each do |item|
    if item.class == Array
      flat_arr.concat(flatten(item))
    else
      flat_arr << item
    end
  end
  return flat_arr
end


flatten([1,'Hello',true,[2,3,4]])
flatten([1,'Hello',true,[2,3,4],[7,3,4],[7,3,9]])
