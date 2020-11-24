# vigenere_cipher
def new_alph(ch):
    alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    new_alph = alph[alph.index(ch):] + alph[:alph.index(ch)]
    return new_alph
    
   
def encrypt(text, big_key):
    res = ''
    alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    i = 1
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1 :
                res += new[alph.index(t)]
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1    
    return res
    
    
def decrypt(text, big_key):
    res = ''
    alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    i = 1
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1 :
                res += alph[new.index(t)]
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1    
    return res    
    
# Put your text
text1 = 'Cryptographie'
text_dec = 'OrRwPsHjmpApA'
# Put your key 
key = 'mathweB2'

if len(key) <= len(text1):
    big_key = key * (len(text1) // len(key)) + key[:len(text1) % len(key)]
    text_encrypt = encrypt(text1, big_key)
    text_decrypt = decrypt(text_dec, big_key)
    
    print('#======Vigenere Cipher ======#')
    print('|----------------------------|')
    print('#========Start Encrypt=======#') 
    print('|Your text: "' + text1 + '"')
    print('|Your key : "' + key + '"')
    print('|Res      : ' + text_encrypt)
    print('|----------------------------|')
    print('#========Start Decrypt=======#')
    print('|Your text: "' + text_dec + '"')
    print('|Your key : "' + key + '"')
    print('|Res      : ' + text_decrypt)
    print('#----------------------------#\n')
    
else:
    print('Error: len(key)>len(text) ')
