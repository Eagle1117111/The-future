import random
import string

characters =  " " +  string.punctuation + string.digits + string.ascii_letters
characters = list(characters)
key = characters.copy()

random.shuffle(key)

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = characters.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")