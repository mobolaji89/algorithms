def fib(n)
  return n if n == 0 || n == 1 # base case
  return fib(n-1) + fib(n-2)
end

fib(10)
