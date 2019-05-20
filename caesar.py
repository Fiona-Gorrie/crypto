lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = lower_alphabet.upper()

def alphabet_position(letter):
    if letter in lower_alphabet:
        return lower_alphabet.find(letter)
 
    return upper_alphabet.find(letter)

def rotate_character(char, rot):
    rot_idx = (alphabet_position(char) + alphabet_position(rot)) % 26

    if char.islower():
        return lower_alphabet[rot_idx]

    if char.isupper():
        return upper_alphabet[rot_idx]

    return char

def encrypt(message, key):
    encrypted_message = "" 
    key_idx = [alphabet_position(letter) for letter in key]
    key_len = len(key)
    message_idx = [alphabet_position(letter) for letter in message]
    for i in range(len(message_idx)):
        encrypted_message += rotate_character(message[i], key[i % len(key)])
    return encrypted_message


print(encrypt("plaintext", "key"))
print(encrypt("PlaintexT", "key"))
print(encrypt("1PlaintexT", "key"))
print(encrypt("1Plain texT", "key"))
