import random
a = [ "07", "31", "50", "63", "66", "77", "84" ]
b = [ "11", "64" ]
c = [ "17", "33", "49" ]
d = [ "10", "27", "51", "76" ]
e = [ "25", "26", "28", "32", "48", "67", "69", "72", "75", "79", "82", "85" ]
f = [ "08", "09" ]
g = [ "44", "83" ]
h = [ "19", "20", "21", "54", "70", "87" ]
i = [ "02", "03", "29", "53", "68", "73" ]
j = [ "18" ]
k = [ "41" ]
l = [ "42", "81", "86", "95" ]
m = [ "40", "52" ]
n = [ "00", "43", "80", "88", "89" ]
o = [ "16", "30", "61", "65", "91", "94", "96" ]
p = [ "01", "62" ]
q = [ "15" ]
r = [ "04", "24", "39", "58", "71", "99" ]
s = [ "06", "34", "56", "57", "59", "90" ]
t = [ "05", "23", "35", "37", "38", "60", "74", "78", "92" ]
u = [ "13", "14", "36" ]
v = [ "22" ]
w = [ "45", "46" ]
x = [ "12" ]
y = [ "55", "93" ]
z = [ "47" ]

theLists = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
AlphabetASCII =[]
for x in range(26):
    AlphabetASCII.append(x+ 97) #remplissage de a à z (ascii code)

def Decrypt(cipherText):
    decryptedMessage =""
    print(cipherText)
    cipherTextSplited = cipherText.split()    
    for i in range(len(cipherTextSplited)): 
        #print("Decoding element : "+cipherTextSplited[i]) 
        for j in range(len(theLists)): 
    
            if theLists[j].__contains__(cipherTextSplited[i]):
                #print(chr(97+j))
                decryptedMessage += str(chr(97+j))

    print("Decrypted Message : "+decryptedMessage)



def Encrypt(clearText):
    EncryptedMessage = ""
    SplitedToCharacters = list(clearText)
    for i in range(len(SplitedToCharacters)):
        character = ord(SplitedToCharacters[i])
        indexCharacter = AlphabetASCII.index(character)
        #print(indexCharacter)
        tempList = theLists[indexCharacter]
        EncryptedMessage += random.choice(tempList)+" "
    print(EncryptedMessage)

Decrypt("87 72 42 95 30")
#Encrypt("hello")

