# Write a function is_even(n) that returns True if n is even and False if n is odd.

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Write a function is_prime(n) that returns True if n is a prime number and False otherwise.

def is_prime(n):
    if n <= 1:
        print("False")
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
           print("False")
        else:
            print("True")

# Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.\
def primes_up_to_n():
    n = int(input("Enter a number: "))
    primes = [x for x in range(2, n + 1) if is_prime(x)]
    return primes


# 5. Function that returns the lesser of two even numbers, or the greater if one or both are odd
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


# 6. Function to check if both words start with the same letter
def is_alliteration(me):
    words = me.lower().split()
    a,b = words
    if a[0] == b[0]:
        return True

# 7. Function to capitalize the first and fourth letters of a name
def old_macdonald(name):
    if len(name) < 4:
        return name.capitalize()
    return name[:3].capitalize() + name[3:].capitalize()



f = old_macdonald("ratrabbit")
print(f)