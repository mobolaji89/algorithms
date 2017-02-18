# Introduction to Algorithm Analysis and Big O

# Functions that sum the numbers from 0 to N

#Function 1
def sum1(n):
  final_sum = 0

  for x in range(n+1):
    final_sum += x

  return final_sum

print(sum1(10)) #55

#Function 2
def sum2(n):
    return (n*(n+1))/2

print(sum2(10)) #55

# Function 2 is much more efficient, running at a much faster rate than the first. However, we can not use time to run as an objective measurement, because that will depend on the speed of the computer itself and hardware capabilities. Therefore, we need to use Big O.
