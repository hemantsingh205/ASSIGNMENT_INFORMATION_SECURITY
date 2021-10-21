import numpy as np
# function to find the index of a character
def indexOf(alphabet):
    return ord(alphabet) - 65


# function to get character from an index
def getAlphabet(index):
    return chr(index + 65)


# function to encrypt using additive cipher
def encryptAdditiveCipher(plaintext_1, key):
    encryptedText = ""
    plaintext=plaintext_1.upper()
    for alphabet in plaintext:
        encryptedText += getAlphabet((indexOf(alphabet) + key) % 26)
    return encryptedText


# function to decrypt in Additive Cipher
def decryptAdditiveCipher(encryptedText_1, key):
    decryptedText = ""
    encryptedText=encryptedText_1.upper()
    for alphabet in encryptedText:
        index = indexOf(alphabet) - key
        if index < 0:
            index += 26
        index %= 26
        decryptedText += getAlphabet(index)
    return decryptedText
print("*****ENCRYPTION*****")
print("SAMPLE INPUT :")
print("Plain Text   : SAWAN")
print("Additve key  : 21")
print("SAMPLE OUTPUT:: ")
print(encryptAdditiveCipher("SAWAN", 21))

print()

print("*****DECRYPTION*****")
print("SAMPLE INPUT :")
print("Cipher Text  : NVRVI")
print("Additve key  : 21")
print("SAMPLE OUTPUT:: ")
print(decryptAdditiveCipher("NVRVI", 21))
print()

#Taking User input :
user_input=input("Enter text for encrypting : ")
user_additive_key=input("Enter the additive key : ")

print("*****ENCRYPTION*****")
print("Your input:: ")
print("Plaine text  : "+user_input)
print("Additive key : "+str(user_additive_key))
print("Your Output:: ")
print("Encrypted  : ", end=" ")
print(encryptAdditiveCipher(user_input,int(user_additive_key)))
print()

print("*****DECRYPTION*****")
user_input=input("Enter text for decrypting : ")
user_additive_key=input("Enter the additive key : ")

print("Your input:: ")
print("Cipher text  : "+user_input)
print("Additive key : "+str(user_additive_key))
print("Your Output::")
print("Decrypted  : ", end=" ")
print(decryptAdditiveCipher(user_input,int(user_additive_key)))

