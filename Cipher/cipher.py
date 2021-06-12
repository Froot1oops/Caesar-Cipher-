def Encryption(plain_text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plain_text = ''.join(plain_text.split()).lower() #removes all whitespace character from string text
    encrypt_text = ''
    for i in plain_text:
        index = alphabet.find(i) #finds index of char in plain_text in alphabet
        new_index = (index + key) % 26 #creates new index using key
        encrypt_text+=alphabet[new_index].upper() #adds new char using new index from alphabet
    return (encrypt_text)
    
def Decryption(plain_text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plain_text = plain_text.lower()
    decrypted_text = ''
    for i in plain_text:
        if i == " ": 
            decrypted_text+= " "
        else:
            index = alphabet.find(i) #finds index of char in plain_text in alphabet
            new_index = (index - key) % 26 #creates new index using key
            decrypted_text+=alphabet[new_index].upper() #adds new char using new index from alphabet
    return (decrypted_text)
