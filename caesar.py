def alphabet_position(letter):
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in lower_alphabet:
        char_idx= lower_alphabet.find(letter)
    else:
        char_idx= upper_alphabet.find(letter)    
    return char_idx   

def rotate_character(char, rot):
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    double_lower_alphabet = lower_alphabet * 2
    double_upper_alphabet = upper_alphabet * 2
    result = ""
    char_idx = alphabet_position(char)
    rot_idx = alphabet_position(rot % 26) 
    if char in lower_alphabet:
        result += double_lower_alphabet[rot_idx]
    elif char in upper_alphabet:
        result += double_upper_alphabet[rot_idx]
    else:
        result += char
    return result 

def encrypt(message, key):
    encrypted_message = []
    key_idx = [alphabet_position(letter) for letter in key]
    key_len = len(key)
    message_idx = [alphabet_position(message) for letter in message]
    for i in range(len(message_idx)):
        encrypted_message.append(rotate_character(message[i], key[i]))
    return encrypted_message


print(encrypt("plaintext", "key"))


#def main():
    #print(encrypt())

#if __name__ == "__main__":
    #main()  
