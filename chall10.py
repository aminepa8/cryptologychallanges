def encryption_CTR(M,key):
    cipher=""
    while len(M)%len(key)!=0:
        M+=" "
    counter=0
    blocks=[M[i:i+len(key)] for i in range(0,len(M)-len(key)+1,len(key))]
    for bloc in blocks:
        temp=rot(key,counter)
        for i in range(len(temp)):
            cipher+=format(ord(temp[i])^ord(bloc[i]),'#04x')
        counter+=1
    return cipher.replace("0x","")

def decryption_CTR(cipher,key):
    M=""
    counter=0
    cipher=[int(str(cipher[i:i+2]),16) for i in range(0,len(cipher)-1,2)]
    blocks=[cipher[i:i+len(key)] for i in range(0,len(cipher)-len(key)+1,len(key))]
    for bloc in blocks:
        temp=rot(key,counter)
        for i in range(len(temp)):
            M+=chr(ord(temp[i])^bloc[i])
        counter+=1
    return M
def rot(text,shift):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output=""
    for x in text:
        if x in alphabet:
            output+=alphabet[(ord(x)-97+shift)%26]
        elif x in ALPHABET:
            output+=ALPHABET[(ord(x)-65+shift)%26]
        else:
            output+=x
    return output
while(1):
    i=int(input("cliquer 1 pour crypter ou 2 pour decrypter: "))
    if i==1:
        message=str(input("saisir le texte a crypter : "))
        key=str(input("entrer la clé: "))
        print(encryption_CTR(message,key))
    elif i==2:
        cipher=str(input("entrer le texte a décrypter "))
        key=str(input("entrer la clé "))
        print(decryption_CTR(cipher,key))

