def encrypt_vigenere(plaintext, key, alphabet):
    ciphertext = ""
    key_index = 0

    for char in plaintext:
        if char in alphabet:
            shift = alphabet.index(key[key_index])
            char_index = alphabet.index(char)
            encrypted_index = (char_index + shift) % len(alphabet)
            ciphertext += alphabet[encrypted_index]
            key_index = (key_index + 1) % len(key)

    return ciphertext

# Intro!!
if __name__ == "__main__":
    alphabet = ""
    plaintext = input('Please insert the plaintext : ')
    key = input('Please insert the key : ')
    lenAlphabet = input('Please insert alphabet len (26|27) : ')

    if (lenAlphabet == "26"):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

    result = encrypt_vigenere(plaintext=plaintext, key=key, alphabet=alphabet)
    print(result)
