# playfair cipher
matrix=[['M','A','R','O','C'],['B','D','E','F','G'],['H','I','J','K','L'],['N','P','Q','S','T'],['U','V','X','Y','Z']]

#fonction pour éliminer le doublon dans la phrase
def identique(phrase,n):
    new_phrase=[]
    if n==0:
        i=0
        while i<len(phrase)-1:
            if phrase[i]==phrase[i+1]:
                new_phrase.append(phrase[i])
                new_phrase.append('X')
                i=i+1
            else:
                new_phrase.append(phrase[i])
                new_phrase.append(phrase[i+1])
                i=i+2
        if i==len(phrase)-1:
            new_phrase.append(phrase[i])
    elif n==1:
        i=0
        while i<len(phrase)-1:
            if i>0 and phrase[i-1]==phrase[i+1] and phrase[i]=='X':
                pass
            else:
                new_phrase.append(phrase[i])
            i=i+1
        if phrase[len(phrase)-1]!='X':
            new_phrase.append(phrase[len(phrase)-1])
    return new_phrase

#fonction pour chiffrie deux lettre avec la methode de playfair
def lettre_chiffre(a,b):
    s=[]
    i1, j1, i2, j2, =0, 0, 0, 0
    for i in range(0,5):
        for j in range(0,5):
            if a==matrix[i][j]:
                i1=i
                j1=j
                break
    for i in range(0,5):
        for j in range(0,5):
            if b==matrix[i][j]:
                i2=i
                j2=j
                break
    if i1==i2:
        s.append(matrix[i1][(j1+1)%5])
        s.append(matrix[i2][(j2+1)%5])
    elif j1==j2:
        s.append(matrix[(i1+1)%5][j1])
        s.append(matrix[(i2+1)%5][j2])
    else:
        s.append(matrix[i1][j2])
        s.append(matrix[i2][j1])
    return s



#fonction pour dechiffrie deux lettre avec la methode de playfair
def lettre_dechiffre(a,b):
    s=[]
    i1, j1, i2, j2, =0, 0, 0, 0
    for i in range(0,5):
        for j in range(0,5):
            if a==matrix[i][j]:
                i1=i
                j1=j
                break
    for i in range(0,5):
        for j in range(0,5):
            if b==matrix[i][j]:
                i2=i
                j2=j
                break
    if i1==i2:
        s.append(matrix[i1][(j1-1)%5])
        s.append(matrix[i2][(j2-1)%5])
    elif j1==j2:
        s.append(matrix[(i1-1)%5][j1])
        s.append(matrix[(i2-1)%5][j2])
    else:
        s.append(matrix[i1][j2])
        s.append(matrix[i2][j1])
    return s
        

#fonction pour chiffrie une phrase avec la methode de playfair
def playfair_chiffre_phrase(phrase):
    phrase_cryptee=[]
    i=0
    phrase_non_identique=identique(phrase,0)
    if len(phrase_non_identique)%2==1:
        phrase_non_identique.append('X')
    for i in range(0,len(phrase_non_identique)-1,2):
        p=lettre_chiffre(phrase_non_identique[i],phrase_non_identique[i+1])
        phrase_cryptee.append(p[0])
        phrase_cryptee.append(p[1])
        i=i+1
    phrase_cryptee="".join(phrase_cryptee)
    return(phrase_cryptee)

#fonction pour dechiffrie une phrase avec la methode de playfair
def playfair_dechiffre_phrase(phrase):
    phrase_decryptee=[]
    for i in range(0,len(phrase)-1,2):
        p=lettre_dechiffre(phrase[i],phrase[i+1])
        phrase_decryptee.append(p[0])
        phrase_decryptee.append(p[1])
    phrase_decryptee=identique(phrase_decryptee,1)
    phrase_decryptee="".join(phrase_decryptee)
    return(phrase_decryptee)


#test
phrase=input("Entrer une phrase:")
print("Phrase:%s\n" %phrase)
p_cryptee=playfair_chiffre_phrase(phrase)
print("phrase_cryptee:%s\n" %p_cryptee)
p_decryptee=playfair_dechiffre_phrase(p_cryptee)
print("phrase_decryptee:%s\n" %p_decryptee)
