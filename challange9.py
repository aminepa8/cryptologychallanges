from itertools import cycle

def split_string(key,Plain_Text):
    n = len(key)
    splited_list_out = [(Plain_Text[i:i+n]) for i in range(0, len(Plain_Text), n)] 
    print("Splited List : ",splited_list_out)
    return splited_list_out


def Encrpyt(key,Plain_Text):
    EncryptedData = []
    Splited_Text = split_string(key,Plain_Text)
    tempKey = key
    for blockData in Splited_Text:
        encrypted = [ a ^ b for (a,b) in zip(bytes(blockData, 'utf-8'),cycle(bytes(tempKey, 'utf-8'))) ]
        tempKey = bytes(encrypted).decode()
        print(encrypted)
        EncryptedData.append(encrypted)
    
    ListMerges = []
    for i in EncryptedData :
        ListMerges += i
    return ListMerges


def Decrpyt(key,Cipher_Text):
    DecryptedData = []
    CipherText = bytes(Cipher_Text).decode()
    Splited_Text = split_string(key,CipherText)
    tempKey = key
    for EncryptedblockData in Splited_Text:
        decrypted = [ a ^ b for (a,b) in zip(bytes(EncryptedblockData,'utf-8'), cycle(bytes(tempKey, 'utf-8'))) ]
        tempKey = bytes(Encrpyt(tempKey,bytes(decrypted).decode('utf-8'))).decode('utf-8')

        DecryptedData.append(decrypted)
    print(decrypted)
    ListMerges = []
    for i in DecryptedData :
        ListMerges += i
    print(ListMerges)
    return ListMerges


cipher=Encrpyt('xyza','hellmedaspothajo')
print(cipher)
Dec = Decrpyt('xyza',cipher)
print(bytes(Dec).decode())




