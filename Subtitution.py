import random   # Import this Lib
import string   # Import this Lib

# Define the character type that will be used to manipulate the input
Chars_= string.punctuation + string.ascii_uppercase + string.ascii_lowercase + string.digits + " "

# Make a list of these characters, giving them each a own identity
Char=list(Chars_)

# Define a Key that will be used to encrypt and decrypt
Key= list(Chars_)

# Shuffel the key, to generate a random set of keys every time the program is excuted
random.shuffle(Key)

# Encrryption 

Plain_Text = input("Enter the Text:")  
Cipher_Text = ""

# Define a that encrypts the input
for letter in Plain_Text:
    index= Char.index(letter)
    Cipher_Text += Key[index]

print(f"Input Orriginal Plain Text:",Plain_Text)
print(f"Encrypted Cipher Text:",Cipher_Text)

# Decryption

Cipher_Text = input("Enter the Text:")
Plain_Text = ""

# Define a that decrypts the input
for letter in Cipher_Text:
    index= Key.index(letter)
    Plain_Text += Char[index]

print(f"Input Cipher Text:",Cipher_Text)
print(f"Decrypted Original Text:",Plain_Text)