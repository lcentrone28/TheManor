import string

def encrypt(msg, shift):
    alphabet = string.ascii_uppercase
    encrypted_msg = ""

    for char in msg:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % 26
            encrypted_msg += alphabet[new_index]
        else:
            encrypted_msg += char

    return encrypted_msg

# print(encrypt("abcd", 30))

def decrypt(msg, shift):
    alphabet = string.ascii_uppercase
    decrypted_msg = ""

    for char in msg:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index - shift) % 26
            decrypted_msg += alphabet[new_index]
        else:
            decrypted_msg += char

    return decrypted_msg

# print(decrypt("abcd", 30))