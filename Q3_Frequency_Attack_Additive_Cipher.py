ALPHABET=" ABCDEFGHIJKLMNOPQRSTUV"   #taken all the lettter of english alhphabet in alphabetical order 
#this function calculates the frequecy of the each letter present in the cipher text given.
def frequency_analysis(cipher_text):
    cipher_text=cipher_text.upper()      #converting all the letters present in the cipher text in Upper case format and removing      
                                         #the case of case sensitivity.
    letter_frequency={}                  #declaring a dictionary for the storage of frequency of all the lettters present in the cipher 
                                         #text.
    
    for letter in ALPHABET:              #this loop is basically for assigning a zero value to  all the 27 characters present in the
        letter_frequency[letter]=0       #ALPHABET variable declared at the top including the whitespace.
    

    for letter in cipher_text:           #Calculating the frequency of each of the characters.

        if letter in ALPHABET:
            letter_frequency[letter]+=1  #if the character is found increasing it's count.
    
    #returning the dictionary in descending order according to the frequency of the characters.
    return dict(sorted(letter_frequency.items(), key=lambda item: item[1], reverse=True) )

#additive encryption algorithm
def additive_encrypt(plain_text, key):

     #the encrypted message
     cipher_text=''
     #making the text in plain_text variable to upper case
     plain_text=plain_text.upper()
     
     for c in plain_text:
         index=ALPHABET.find(c)

         index= (index+key)%len(ALPHABET)

         cipher_text=cipher_text+ ALPHABET[index]
    
     return cipher_text

#this function decrypt the cipher text.
def additive_decrypt(cipher_text1,key):

    plain_text=""                               
    cipher_text=cipher_text1.upper()               #Making all the letters to uppper case.
    
    for c in cipher_text:                          #travesing the cipher text.  
        if c==' ':                                 #if whitespace is found adding it to the plain text as it.
            plain_text+=' '
            pass                                   #if whitespace is found it is just added to the plain text variable no other  
                                                   #operation is done.
                                                   
        if c!=' ':
            index=ALPHABET.find(c)                 #locating the index of a paritcular letter in cipher text.
        
            index=(index-key)%len(ALPHABET)        #decrypting it by additive cipher.
            plain_text=plain_text+ALPHABET[index]  #adding the decrypted letter to the plain_text variable.

    return plain_text

#main funciton.
if __name__=="__main__":
    #Sample INPUT
    text="efgfoe uif fbtu xbmm pg uif dbtumf "
    frequency_cipher={}
    frequency_cipher=frequency_analysis(text)
    
    #Sample OUTPUT
    #Top ten possible plain text 
    print("Sample INPUT : "+ text)
    print("Sample OUTPUT : ")
    print("Key : Frequency : Plain Text ")
    for i in range(0,10):
        key_calculate=ALPHABET.find(list(frequency_cipher)[i]) - ALPHABET.find("E")
        print(list(frequency_cipher)[i]+"   :   "+ str(frequency_cipher[list(frequency_cipher)[i]])+"       : ", end=" ")
        print(additive_decrypt(text,key_calculate))
    print()
    

    user_input=input("Enter cipher text : ")
    frequency_cipher={}
    frequency_cipher=frequency_analysis(text)

    #Top ten possible plain text 
    print()
    print("User INPUT : "+ user_input )
    print("Your OUTPUT : ")
    print("Key : Frequency : Plain Text ")
    for i in range(0,10):
        key_calculate=ALPHABET.find(list(frequency_cipher)[i]) - ALPHABET.find("E")
        print(list(frequency_cipher)[i]+"   :   "+ str(frequency_cipher[list(frequency_cipher)[i]])+"       : ", end=" ")
        print(additive_decrypt(user_input,key_calculate))
         
       
