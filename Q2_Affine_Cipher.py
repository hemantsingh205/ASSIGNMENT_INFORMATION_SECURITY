# function to find the index of a character
def indexOf(alphabet):
    return ord(alphabet) - 65


# function to get character from an index
def getAlphabet(index):
    return chr(index + 65)


# function to find multiplicative inverse using Extended Euclidean Algorithm
# return modular multiplicative inverse of ‘x’ under modulo ‘y’
# (x*k) mod y = 1 , where k is the modular multiplicative inverse of ‘x’ under modulo ‘y’
def findMultiplicativeInverse(x, y):
    r1 = y  # larger number
    r2 = x  # smaller number
    t1 = 0
    t2 = 1
    # print('q', 'r1', 'r2', 'r', 't1', 't2', 't')
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        t = t1 - q * t2

        # print(q, r1, r2, r, t1, t2, t)
        r1 = r2
        r2 = r

        t1 = t2
        t2 = t
    if r1 == 1:  # ensuring gcd is 1 for multiplicative inverse to exist
        return t1
    else:
        return False


# function to encrypt using affine cipher
# key1 -> multiplicative key
# key2 -> additive key
# key1 and key2 needs to be different
def encryptAffineCipher(plaintext_1, key1, key2):
    encryptedText = ""
    plaintext=plaintext_1.upper()
    for alphabet in plaintext:
        index = indexOf(alphabet)
        index = (index * key1) % 26  # key1 and 26 needs to be co-prime
        index = (index + key2) % 26
        encryptedText += getAlphabet(index)
    return encryptedText


# function to decrypt using affine cipher
# key1 -> multiplicative key
# # key2 -> additive key
# # key1 and key2 needs to be different
def decryptAffineCipher(encryptedText_1, key1, key2):
    decryptedText = ""
    encryptedText=encryptedText_1.upper()
    for alphabet in encryptedText:
        index = indexOf(alphabet)
        # key2 operations
        index = index - key2
        if index < 0:
            index += 26
        index %= 26
        # key1 operations
        key1MultiplicativeInverse = findMultiplicativeInverse(key1, 26)
        index = index * key1MultiplicativeInverse
        index %= 26

        decryptedText += getAlphabet(index)
    return decryptedText

#Sample Input & Output.
print("*****ENCRYPTION******")
print("SAMPLE INPUT ::")
print("Plain text   : HELLO")
print("SAMPLE OUTPUT :: ")
print(encryptAffineCipher("HELLO", 7, 2))
print()
print("*****DECRYPTION******")
print("SAMPLE INPUT ::")
print("Plain text   : ZWBBW")
print("SAMPLE OUTPUT :: ")
print(decryptAffineCipher("ZEBBW", 7, 2))
print()

#user input
print("*****ENCRYPTION******")
user_input=input("Enter text for encrypting : ")
multiplicative_key=int(input("Enter the multiplicative key : "))
additive_key=int(input("Enter the additive key : "))
print("Your input :: ")
print("Plain text         : "+user_input)
print("Multiplicative Key : "+str(multiplicative_key))
print("Additive Key       : "+str(additive_key))
print("Your Output ::")
print("Encrypted : ", end=" ")
print(encryptAffineCipher(user_input, multiplicative_key, additive_key))

print()

print("*****DECRYPTION******")
user_input=input("Enter text for decrypting : ")
multiplicative_key=int(input("Enter the multiplicative key : "))
additive_key=int(input("Enter the additive key    : "))
print("Your input :: ")
print("Plain text         : "+user_input)
print("Multiplicative Key : "+str(multiplicative_key))
print("Additive Key       : "+str(additive_key))
print("Your Output ::")

print("Decrypted : ", end=" ")
print(decryptAffineCipher(user_input, multiplicative_key, additive_key))
print()