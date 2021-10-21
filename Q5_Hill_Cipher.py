import numpy as np


# function to find the index of a character
def indexOf(alphabet):
    return ord(alphabet) - 65


# function to get character from an index
def getAlphabet(index):
    return chr(index + 65)


# assuming key text is of length 4 and form 2*2 matrix
def getKeyMatrix(key):
    keyMatrix = np.zeros((2, 2))
    keyMatrix[0][0] = int(indexOf(key[0]))
    keyMatrix[0][1] = int(indexOf(key[1]))
    keyMatrix[1][0] = int(indexOf(key[2]))
    keyMatrix[1][1] = int(indexOf(key[3]))
    return keyMatrix


# function to obtain matrix for plaintext
def obtainMatrix(text):
    if len(text) % 2 == 1:
        text += "X"  # appending extra character in case text length is odd
    rows = 2
    rows = int(rows)
    columns = len(text) / 2
    columns = int(columns)
    textMatrix = np.zeros((rows, columns))
    characterPointer = 0
    for column in range(0, columns):
        for row in range(0, rows):
            textMatrix[row][column] = indexOf(text[characterPointer])
            characterPointer += 1
    return textMatrix


# function to find gcd
def findGCD(x, y):
    r1 = x if x > y else y
    r2 = x + y - r1
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        r1 = r2
        r2 = r
    return r1


# function to check if two numbers are co prime
def ifCo_prime(x, y):
    return findGCD(x, y) == 1


# function to multiply matrices
def matrixMultiplication(mat1, mat2):
    dim1 = mat1.shape
    row1 = dim1[0]
    col1 = dim1[1]
    dim2 = mat2.shape
    row2 = dim2[0]
    col2 = dim2[1]
    matProduct = np.empty(shape=(row1, col2), dtype='object')
    matProduct.fill(0)
    if col1 == row2:
        for i in range(row1):
            for j in range(col2):
                for k in range(row2):
                    matProduct[i][j] = matProduct[i][j] + \
                        (mat1[i][k] * mat2[k][j])
        return matProduct
    else:
        print("Matrices are not compatible for multiplication. ")


# Function to perform encryption in Hill Cipher
def encryptHillCipher(plaintext, key):
    keyMatrix = getKeyMatrix(key)
    plaintextMatrix = obtainMatrix(plaintext)
    rows = keyMatrix.shape[0]
    columns = plaintextMatrix.shape[1]
    # encryptedMatrix = np.empty(shape=(rows, columns), dtype='object')
    encryptedMatrix = matrixMultiplication(keyMatrix, plaintextMatrix)
    # print(encryptedMatrix)
    encryptedText = ""
    for column in range(0, columns):
        for row in range(0, rows):
            encryptedMatrix[row][column] %= 26
            encryptedText += getAlphabet(int(encryptedMatrix[row][column]))
    # print(encryptedMatrix)
    return encryptedText


def determinant(mat):
    det1 = 0
    dim = mat.shape
    if dim[0] == dim[1]:
        n = dim[0]
        if n == 2:
            det1 = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        else:
            print("Please keep the order of matrix 2*2 for determinant calculation ")
    else:
        print("Matrix given is not a square matrix . Determinant can be calculated only for a square matrix .")
    return det1


# function to find multiplicative inverse using Extended Euclidean Algorithm
# return modular multiplicative inverse of ‘a’ under modulo ‘m’
# (a*k) mod m = 1 , where k is the modular multiplicative inverse of ‘a’ under modulo ‘m’
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


# function to find the adjoint of a matrix
def findAdjointOfMatrixOfOrder2(matrix):
    adjointMatrix = np.empty(shape=(2, 2), dtype='object')
    adjointMatrix[0][0] = matrix[1][1]
    adjointMatrix[0][1] = -matrix[0][1]
    adjointMatrix[1][0] = -matrix[1][0]
    adjointMatrix[1][1] = matrix[0][0]
    return adjointMatrix


# function to remove negative elements from the matrix by adding +26
def add26RemoveNegative(matrix):
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    for row in range(0, rows):
        for column in range(0, columns):
            if matrix[row][column] < 0:
                matrix[row][column] += 26
    return matrix


# function to multiply matrix by a scalar
def multiplyMatrixByScalar(matrix, scalar):
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    for row in range(0, rows):
        for column in range(0, columns):
            matrix[row][column] *= scalar
    return matrix


# function to remove negative elements from the matrix by adding +26
def applyMOD26(matrix):
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    for row in range(0, rows):
        for column in range(0, columns):
            matrix[row][column] %= 26
    return matrix


# function to check if key is valid
def isValidKey(key):
    keyMatrix = getKeyMatrix(key)
    determinantOfKeyMatrix = determinant(keyMatrix)
    return ifCo_prime(determinantOfKeyMatrix, 26)


# function to perform decryption in Hill Cipher
def decryptHillCipher(encryptedText, key):
    encryptedTextMatrix = obtainMatrix(encryptedText)
    # print(encryptedTextMatrix)
    keyMatrix = getKeyMatrix(key)
    # print(keyMatrix)
    determinantOfKeyMatrix = determinant(keyMatrix)
    # determinantOfKeyMatrix %= 26
    # print(determinantOfKeyMatrix)
    if determinantOfKeyMatrix:  # ensuring determinant is not zero, i.e. matrix is  invertible
        # print("determinant of key matrix:", determinantOfKeyMatrix)
        multiplicativeInverseOfDeterminant = findMultiplicativeInverse(
            determinantOfKeyMatrix, 26)
        # print(multiplicativeInverseOfDeterminant)
        adjointKeyMatrix = findAdjointOfMatrixOfOrder2(keyMatrix)
        # now removing negative values in the adjoint matrix by adding +26 to negative elements
        adjointKeyMatrix = add26RemoveNegative(adjointKeyMatrix)
        # finding inverse key matrix
        inverseKeyMatrix = multiplyMatrixByScalar(
            adjointKeyMatrix, multiplicativeInverseOfDeterminant)
        # apply modulo 26 on each element of the inverseKeyMatrix
        inverseKeyMatrix = applyMOD26(inverseKeyMatrix)
        # print(inverseKeyMatrix)

        # decryption process
        decryptedTextMatrix = matrixMultiplication(
            inverseKeyMatrix, encryptedTextMatrix)
        decryptedTextMatrix = applyMOD26(decryptedTextMatrix)
        # print(decryptedTextMatrix)

        decryptedText = ""
        rows = decryptedTextMatrix.shape[0]
        columns = decryptedTextMatrix.shape[1]
        for column in range(0, columns):
            for row in range(0, rows):
                # print(decryptedTextMatrix[row][column])
                decryptedText += getAlphabet(
                    int(decryptedTextMatrix[row][column]))
        return decryptedText

# SAMPLE INPUT
print("****ENCRYPTION******")
print("SAMPLE INPUT :: ")
print("Plain text : ATTACK")
print("Default text key : NCDB")
print(encryptHillCipher("ATTACK", "NCDB"))
print()

print("****ENCRYPTION******")
print("SAMPLE INPUT :: ")
print("Plain text : MTNFUQ")
print("Default text key : NCDB")
print(decryptHillCipher("MTNFUQ", "NCDB"))
print()

# USER INPUT
user_input_text = input("Enter the plain text : ")
print("NOTE: Key text must be of length greater than 4 and must be of even length")
user_key_text = input("Enter key text : ")

if(isValidKey(user_key_text)):
    print("****ENCRYPTION******")
    print("Your Input :: ")
    print("Plain Text : "+user_input_text)
    print("Key Text   : "+user_key_text)
    print(encryptHillCipher(user_input_text, user_key_text))
    print()


else:
    print("The key is not valid : ")
    print("Would you like to use default key: ")
    print("Choose 1 : For YES")
    print("Choose 0 : For NO")
    choice =int( input("Enter Your Choice Please: "))
    if(choice == 1):
        print("****ENCRYPTION******")
        print("Your Input :: ")
        print("Plain Text : "+user_input_text)
        print("Default Key Text   : NCDB")
        print(encryptHillCipher(user_input_text, "NCDB"))
        print()
    else:
        print("EXIT: Pls try with a valid key")


user_input_text = input("Enter the decrypted text : ")
print("NOTE: Key text must be of length greater than 4 and must be of even length")
user_key_text = input("Enter key text : ")

if(isValidKey(user_key_text)):
    print("*****DECRYPTION******")
    print("Your Input :: ")
    print("Plain Text : "+user_input_text)
    print("Key Text   : "+user_key_text)
    print(decryptHillCipher(user_input_text, user_key_text))
    print()


else:
    print("The key is not valid : ")
    print("Would you like to use default key: ")
    print("Choose 1 : For YES")
    print("Choose 0 : For NO")
    choice = int(input("Enter Your Choice Please: "))
    if(choice == 1):
        print("*****DECRYPTION******")
        print("Your Input :: ")
        print("Plain Text : "+user_input_text)
        print("Default Key Text   : NCDB")
        print(decryptHillCipher(user_input_text, "NCDB"))
        print()
    else:
        print("EXIT: Pls try with a valid key")

