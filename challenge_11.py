#RC4 encryption and decryption

#key 
k=[3,1,4,1,5]

def encrypt_decrypt(M):
    # S-array of length n and The temporary vector

    s=[]
    n=8
    T=[]
    for i in range(0,n):
        s.append(i)
        p=i%len(k)
        T.append(k[p])


    #KSA
    j=0
    for i in range(0,n):
        j=(j+s[i]+T[i])%n
        c=s[i]
        s[i]=s[j]
        s[j]=c


    #PRGA Generating Key Stream
    C=[]
    i=0
    j=0
    for l in range(0,len(M)):
        i=(i+1)%n
        j=(j+s[i])%n
        c=s[i]
        s[i]=s[j]
        s[j]=c
        key=(s[i]+s[j])%n
        ci=M[l]^s[key]
        C.append(ci)
    return C

#test

M=[6,1,5,4]
print("Phrase:%s\n" %M)
p_cryptee=encrypt_decrypt(M)
print("phrase_cryptee:%s\n" %p_cryptee)

p_decryptee=encrypt_decrypt(p_cryptee)
print("phrase_decryptee:%s\n" %p_decryptee)


