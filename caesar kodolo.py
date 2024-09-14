string = "gyakorlas!! ! ! 123"
shift = 2
def encryptor(string, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for letter in string:
        if not letter.isalpha():
            encrypted += letter
        else:
            index = alphabet.find(letter.lower())
            shifted_index = (index + shift) % len(alphabet)
            encrypted += alphabet[shifted_index]
    print (encrypted)
encryptor('Encrypt me', 2)

