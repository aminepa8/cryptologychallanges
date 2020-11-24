from itertools import cycle
var="hello"
key="xy"
print(var)
encrypted = [ a ^ b for (a,b) in zip(bytes(var, 'utf-8'),cycle(bytes(key, 'utf-8'))) ]
print(encrypted)

decrypted = [ a ^ b for (a,b) in zip(bytes(encrypted), cycle(bytes(key, 'utf-8'))) ]
print(decrypted)

print(bytes(decrypted))

print(bytes(decrypted).decode())


print(bytearray(16))

'''
# 0 XOR 0  = 0
# 1 XOR 1  = 0
# 0 XOR 1  = 1
# 1 XOR 0  = 1
import base64

def byte_xor(ba1, ba2):
    """ XOR two byte strings """
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])



def split_string(key,Plain_Text):
     # split Plain_Text by the lengh of the key  
    
    # Defining splitting point 
    n = len(key)
    
    # Using list comprehension 
    splited_list_out = [(Plain_Text[i:i+n]) for i in range(0, len(Plain_Text), n)] 

    # the blocks shoud have the same length as the key , so will add space to complete 
    #for blockOfString in splited_list_out:
    for i in range(0, len(splited_list_out)):
        diff_length = len(key) - len(splited_list_out[i])
        if diff_length > 0:
            splited_list_out[i] = splited_list_out[i] + ' '*diff_length # adding space char so that len(key) = len(block)
    print("Splited List : ",splited_list_out)
    return splited_list_out
    


def Encrpyt(key,Plain_Text):
    #key is the initializaed key
    tempKey = key.encode()
    packet_bytes = bytearray()
    """
    docstring
    """
    list_of_string_blocks = split_string(key,Plain_Text)
    for i in range(0, len(list_of_string_blocks)):
       blockStr = list_of_string_blocks[i]
       print("Block String : " +blockStr)
       tempKey = byte_xor(tempKey,blockStr.encode())
       packet_bytes += bytearray(tempKey)
       print(tempKey)
    return packet_bytes

def toString(string):    
    try:
        return string.decode("utf-8")
    except ValueError:
        return string

#print(Encrpyt('xor','amines'))
#encoded = base64.b64encode(Encrpyt('xor','amines'))
#print(toString(encoded))
#cipherText = toString(encoded)

#print(Encrpyt('xor',cipherText))

key = 'xor'
plainText = 'ami'
#print(toString(base64.b64encode(byte_xor(key.encode(),plainText.encode()))))

cipherText = byte_xor(key.encode(),plainText.encode())
print(cipherText)
print(toString(base64.b64encode(byte_xor(key.encode(),cipherText))))
'''