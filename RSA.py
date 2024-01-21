import random 
import math

def is_a_prime(num):
    if num<2:
        return False
    for i in range (2, num // 2 + 1 ):
        if num %i == 0:
            return False
    return True 

def create_prime(min_prime, max_prime):
    prime = random.randint(min_prime, max_prime)
    while not is_a_prime(prime):
        prime = random.randint(min_prime, max_prime)
    return prime 

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d*e)%phi == 1:
            return d
    raise ValueError("mod_inverse does not eexist")

p,q = create_prime(1000, 5000), create_prime(1000, 5000)

while p==q:
    q= create_prime(1000, 5000)

n = p*q
phi_n= (p-1)*(q-1)

e= random.randint(3, phi_n-1)
while math.gcd(e, phi_n) !=1:
    e= random.randint(3, phi_n-1)

d= mod_inverse(e, phi_n-1)

print("Public Key: ", e)
print("Private Key: ", d)
print("n: ", n)
print("Phi of n: ", phi_n)
print("p: ", p)
print("q: ", q)

message = "Happy Birthday"

message_encrypt=[ord(ch) for ch in message]

ciphertext= [pow(ch, e, n) for ch in message_encrypt]

print(ciphertext)

message_encrypt= [pow(ch, d, n) for ch in ciphertext]
message = "".join([chr(ch) for ch in message_encrypt if 0 <= ch <= 0x10FFFF ])
print(message)