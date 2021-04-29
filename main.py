# Task Fibonacci sequence
#The method of the Fibonacci sequences
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
#The amount of the term you want 
terms = 20

for i in range(terms):
      #calling the function 
      print(recur_fibo(i), end=" ")













