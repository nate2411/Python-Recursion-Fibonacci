# Task Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

terms = 20

# check if the number of terms is valid
if terms <= 0:
   print("Plese enter a positive integer")
else:

   for i in range(terms):
      print(recur_fibo(i), end=" ")













