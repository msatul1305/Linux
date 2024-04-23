def sieve_of_eratosthenes(n):
    # Create a boolean list "prime[0..n]" and initialize all entries as True
    prime = [True for _ in range(n+1)]
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it's a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Create a list of prime numbers found
    primes = [p for p in range(2, n+1) if prime[p]]
    return primes

# Find prime numbers between 1 and 100
prime_numbers = sieve_of_eratosthenes(100)

# Print the list of prime numbers
print("Prime numbers between 1 and 100:")
print(prime_numbers)
