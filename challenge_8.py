# AES with ECB
from Crypto.Cipher import AES

def encrypt_ECB(msg, key): 
    cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
    msg =cipher.encrypt(msg.encode("utf8"))
    return msg


def decrypt_ECB(msg, key): 
    decipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
    return decipher.decrypt(msg).decode("utf8")

#to test: pwd = abcdefghijklmnop and msg= TechTutorialsX!!

msg = input('Message...: ')
pwd = input('Password..: ')

e=encrypt_ECB(msg, pwd)
d=decrypt_ECB(e, pwd)
print('cipher : ', e.hex())
print('dcipher : ', d)
