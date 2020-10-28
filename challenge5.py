
theAlphabetList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def getAlphaRange(alphaText):
    IndexList = []
    alphaTextToCharacters = list(alphaText)
    for i in range(len(alphaTextToCharacters)):
        charIndex = theAlphabetList.index(alphaTextToCharacters[i].lower()) 
        IndexList.append(charIndex) 
    return IndexList

def EncryptVernam(plainText,EncodeKey):
    print("--------------------------Encryption Vernam--------------------")
    print("Plain text = ",plainText)
    print("Encrypt Key  = ",EncodeKey)
    EncryptedText='' #this will store the encrpted result
    plainTextAlphaRange = getAlphaRange(plainText)
    EncodeKeyAlphaRange = getAlphaRange(EncodeKey)
    if(len(plainTextAlphaRange)==len(EncodeKeyAlphaRange)):
        #print(plainTextAlphaRange)
        #print(EncodeKeyAlphaRange)
        for i in  range(len(plainTextAlphaRange)):
            RangsCleChar = ( plainTextAlphaRange[i]+EncodeKeyAlphaRange[i] ) % 26 # Ci = (Pi + Ri) mod 26
            EncryptedText += theAlphabetList[RangsCleChar] 
        print("Encrypted Text  = ",EncryptedText.upper())
    else:
        print("The PlainText should be equal to the encrypt key")


def DecryptVernam(EncryptedText,EncodeKey):
    print("--------------------------Decryption Vernam--------------------")
    print("Encrypted text = ",EncryptedText)
    print("Encrypt Key  = ",EncodeKey)
    DecryptedText='' #this will store the Decrypted result
    EncryptedTextAlphaRange = getAlphaRange(EncryptedText)
    EncodeKeyAlphaRange = getAlphaRange(EncodeKey)
    if(len(EncryptedTextAlphaRange)==len(EncodeKeyAlphaRange)):

        for i in  range(len(EncryptedTextAlphaRange)):
            RangsCleChar = ( EncryptedTextAlphaRange[i] - EncodeKeyAlphaRange[i] ) % 26 # Pi = (Ci - Ri) mod 26
            DecryptedText += theAlphabetList[RangsCleChar] 
        print("Decrypted Text  = ",DecryptedText.upper())
    else:
        print("The PlainText should be equal to the encrypt key")

#Exec
EncryptVernam('INPT','PLAN')
DecryptVernam('XYPG','PLAN')