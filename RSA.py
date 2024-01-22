import random   # Add the required lib
import math     # Add the required lib

# Define a prime number 
def is_a_prime(num):
    if num<2:
        return False
    for i in range (2, num // 2 + 1 ):
        if num %i == 0:
            return False
    return True 

# Generate Prime numbers, it is a helper 
def create_prime(min_prime, max_prime):
    prime = random.randint(min_prime, max_prime)
    while not is_a_prime(prime):
        prime = random.randint(min_prime, max_prime)
    return prime 

# Definne the mod function for the program to calculate the primes and other required variables
def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d*e)%phi == 1:
            return d
    raise ValueError("mod_inverse does not exist")

# Set a range for Primes, This means that the prime numbers will be generated between 1000-5000
p,q = create_prime(1000, 5000), create_prime(1000, 5000)

# If while Generating Primes p=q then q must be regenrated 
while p==q:
    q= create_prime(1000, 5000)

# Calculation for n 
n = p*q
phi_n= (p-1)*(q-1)

# Calculation for e
e= random.randint(3, phi_n-1)
while math.gcd(e, phi_n) !=1:
    e= random.randint(3, phi_n-1)

# Calculation for d
d= mod_inverse(e, phi_n)

# For the record, you can print and check what is happening 
print("Public Key: ", e)
print("Private Key: ", d)
print("n: ", n)
print("Phi of n: ", phi_n)
print("p: ", p)
print("q: ", q)

# Add a message you want to encrypt 
message = "Happy Birthday"

# Here the message is encoded
message_encrypt=[ord(ch) for ch in message]

# (m ^ e) mod n = c   This encrypts the message 
# pow() means-- (ch ^ e) mod n 
ciphertext= [pow(ch, e, n) for ch in message_encrypt]

print(ciphertext)

# Decrypt the cipher text
message_encrypt= [pow(ch, d, n) for ch in ciphertext]
message = "".join(chr(ch) for ch in message_encrypt )
print(message)
