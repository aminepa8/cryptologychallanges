#hill cipher 9 letter key 
import sys
import numpy as np


def cipher_encryption():
    #Ask the User to Add a Message
    msg = input("Enter message: ").upper()
    #Remove space from the message
    msg = msg.replace(" ", "")

    # if message length is odd number, append 0 at the end
    len_chk = 0
    if len(msg) % 3 == 1:
        msg += "00"
        len_chk = 1
    if len(msg) % 3 == 2:
        msg +="0"
        len_chk = 2
    # msg to matrices
    row = 3
    col = int(len(msg)/3)
    msg3d = np.zeros((row, col), dtype=int)
    
    itr1 = 0
    itr2 = 0
    itr3 = 0
    for i in range(len(msg)):
        if i % 3 == 0:
            msg3d[0][itr1] = int(ord(msg[i])-65)
            itr1 = itr1+1
        elif i % 3 == 1:
            msg3d[1][itr2] = int(ord(msg[i])-65)
            itr2 += 1
        else:
            msg3d[2][itr3] = int(ord(msg[i])-65)
            itr3 += 1     
    # for

    key = input("Enter 9 letter Key String: ").upper()
    key = key.replace(" ", "")

    # key to 3x3
    key3d = np.zeros((3, 3), dtype=int)
    itr4 = 0
    for i in range(3):
        for j in range(3):
            key3d[i][j] = ord(key[itr4])-65
            itr4 += 1

    # checking validity of the key
    # finding determinant
    deter = key3d[0][0]*(key3d[1][1]*key3d[2][2] - key3d[2][1]*key3d[1][2]) - key3d[1][0]*(key3d[0][1]*key3d[2][2] - key3d[2][1]*key3d[0][2]) + key3d[2][0]*(key3d[0][1]*key3d[1][2] - key3d[0][2]*key3d[1][1])
    deter = deter % 26
    
    # finding multiplicative inverse
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    # for

    if mul_inv == -1:
        print("Invalid key")
        sys.exit()
    # if

    encryp_text = ""
    itr_count = int(len(msg)/3)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg3d[0][i] * key3d[0][0] + msg3d[1][i] * key3d[0][1] + msg3d[2][i] * key3d[0][2]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg3d[0][i] * key3d[1][0] + msg3d[1][i] * key3d[1][1] + msg3d[2][i] * key3d[1][2]
            encryp_text += chr((temp2 % 26) + 65)
            temp3 = msg3d[0][i] * key3d[2][0] + msg3d[1][i] * key3d[2][1] + msg3d[2][i] * key3d[2][2]
            encryp_text += chr((temp3 % 26) + 65)
        # for
    elif len_chk == 1:
        for i in range(itr_count-2):
            temp1 = msg3d[0][i] * key3d[0][0] + msg3d[1][i] * key3d[0][1] + msg3d[2][i] * key3d[0][2]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg3d[0][i] * key3d[1][0] + msg3d[1][i] * key3d[1][1] + msg3d[2][i] * key3d[1][2]
            encryp_text += chr((temp2 % 26) + 65)
            temp3 = msg3d[0][i] * key3d[2][0] + msg3d[1][i] * key3d[2][1] + msg3d[2][i] * key3d[2][2]
            encryp_text += chr((temp3 % 26) + 65)
        # for
    else:
        for i in range(itr_count-1):
            temp1 = msg3d[0][i] * key3d[0][0] + msg3d[1][i] * key3d[0][1] + msg3d[2][i] * key3d[0][2]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg3d[0][i] * key3d[1][0] + msg3d[1][i] * key3d[1][1] + msg3d[2][i] * key3d[1][2]
            encryp_text += chr((temp2 % 26) + 65)
            temp3 = msg3d[0][i] * key3d[2][0] + msg3d[1][i] * key3d[2][1] + msg3d[2][i] * key3d[2][2]
            encryp_text += chr((temp3 % 26) + 65)
    # if else
    print("Encrypted Text: {}".format(encryp_text))


def cipher_decryption():
    msg = input("Enter message: ").upper()
    msg = msg.replace(" ", "")

    # if message length is odd number, append 0 at the end
    len_chk = 0
    if len(msg) % 3 == 1:
        msg += "00"
        len_chk = 1
    if len(msg) % 3 == 2:
        msg += "0"
        len_chk = 2

    # msg to matrices
    row = 3
    col = int(len(msg) / 3)
    msg3d = np.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    itr3 = 0
    for i in range(len(msg)):
        if i % 3 == 0:
            msg3d[0][itr1] = int(ord(msg[i])-65)
            itr1 += 1
        elif i % 3 == 1:
            msg3d[1][itr2] = int(ord(msg[i])-65)
            itr2 += 1
        else:
            msg3d[2][itr3] = int(ord(msg[i])-65)
            itr3 += 1
    # for

    key = input("Enter 9 letter Key String: ").upper()
    key = key.replace(" ", "")

    # key to 3x3
    key3d = np.zeros((3, 3), dtype=int)
    itr4 = 0
    for i in range(3):
        for j in range(3):
            key3d[i][j] = ord(key[itr4]) - 65
            itr4 += 1
    # for
    #print('key3d:', key3d)
    # finding determinant
    deter = key3d[0][0]*(key3d[1][1]*key3d[2][2] - key3d[2][1]*key3d[1][2]) - key3d[1][0]*(key3d[0][1]*key3d[2][2] - key3d[2][1]*key3d[0][2]) + key3d[2][0]*(key3d[0][1]*key3d[1][2] - key3d[0][2]*key3d[1][1])
    deter = deter % 26
    # finding multiplicative inverse
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    # for
    if mul_inv == -1:
        print("Invalid key")
        sys.exit()
    #matrix of minors
    key3d_inv = np.zeros((3, 3), dtype=int)
    s=[]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if k!=i and l!=j:
                        s.append(key3d[k][l])
            key3d_inv[i][j]= s[0]*s[3]-s[1]*s[2]
            s=[]
    
    #matrix of cafactors
    for i in range(3):
        for j in range(3):
            if i%2 != j%2:
                key3d_inv[i][j] *= -1

    # adjugate matrix
    key3d_inv[0], key3d_inv[1], key3d_inv[2] = [key3d_inv[0][0],key3d_inv[1][0],key3d_inv[2][0]], [key3d_inv[0][1],key3d_inv[1][1],key3d_inv[2][1]], [key3d_inv[0][2],key3d_inv[1][2],key3d_inv[2][2]]


    
    for i in range(3):
        for j in range(3):
            key3d_inv[i][j] = key3d_inv[i][j] * mul_inv

    
    # modulo
    for i in range(3):
        for j in range(3):
            key3d_inv[i][j] = key3d_inv[i][j] % 26

    # cipher to plain
    decryp_text = ""
    itr_count = int(len(msg)/3)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg3d[0][i] * key3d_inv[0][0] + msg3d[1][i] * key3d_inv[0][1] + msg3d[2][i] * key3d_inv[0][2]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg3d[0][i] * key3d_inv[1][0] + msg3d[1][i] * key3d_inv[1][1] + msg3d[2][i] * key3d_inv[1][2]
            decryp_text += chr((temp2 % 26) + 65)
            temp3 = msg3d[0][i] * key3d_inv[2][0] + msg3d[1][i] * key3d_inv[2][1] + msg3d[2][i] * key3d_inv[2][2]
            decryp_text += chr((temp3 % 26) + 65)
        # for
    elif len_chk == 1:
        for i in range(itr_count-2):
            temp1 = msg3d[0][i] * key3d_inv[0][0] + msg3d[1][i] * key3d_inv[0][1] + msg3d[2][i] * key3d_inv[0][2]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg3d[0][i] * key3d_inv[1][0] + msg3d[1][i] * key3d_inv[1][1] + msg3d[2][i] * key3d_inv[1][2]
            decryp_text += chr((temp2 % 26) + 65)
            temp3 = msg3d[0][i] * key3d_inv[2][0] + msg3d[1][i] * key3d_inv[2][1] + msg3d[2][i] * key3d_inv[2][2]
            decryp_text += chr((temp3 % 26) + 65)
        # for
    else:
        for i in range(itr_count-1):
            temp1 = msg3d[0][i] * key3d_inv[0][0] + msg3d[1][i] * key3d_inv[0][1] + msg3d[2][i] * key3d_inv[0][2]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg3d[0][i] * key3d_inv[1][0] + msg3d[1][i] * key3d_inv[1][1] + msg3d[2][i] * key3d_inv[1][2]
            decryp_text += chr((temp2 % 26) + 65)
            temp3 = msg3d[0][i] * key3d_inv[2][0] + msg3d[1][i] * key3d_inv[2][1] + msg3d[2][i] * key3d_inv[2][2]
            decryp_text += chr((temp3 % 26) + 65)
    # if else

    print("Decrypted Text: {}".format(decryp_text))


def main():
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        print("---Encryption---")
        cipher_encryption()
    elif choice == 2:
        print("---Decryption---")
        cipher_decryption()
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()
