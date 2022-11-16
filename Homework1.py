# First of all, I need to check whether a given number is a prime number
def isprime(n):
    # Both 0 and 1 are not prime numbers, so I am excluding them at the very beginning
    if(n == 0 or n == 1):
        return False

    for k in range (2, n):
        # Here I will use modulo to check whether it is possible to divide n by k
        # If so, then n is not prime
        if (n % k == 0):
            return False
    # If it is not dividable then it is a prime number
    return True

# The final code
N = 100
# Now I will check all numbers from 2 to N (I am starting with 2 since 1 is not a prime number)
for k in range(2, N+1):
    if (isprime(k)):
        print(k)