def cipher_encryption():

    msg = input("The text : ").replace(" ", "#").upper()
    key = input("The keyword : ").upper()

    m = keyword_num_assign(key)

    for i in range(len(key)):
        print(key[i], end=" ", flush=True)

    print()
    for i in range(len(key)):
        print(str(m[i]), end=" ", flush=True)

    print()
    print("-------------------------")


    extra_letters = len(msg) % len(key)

    dummy_characters = len(key) - extra_letters


    if extra_letters != 0:
        for i in range(dummy_characters):
            msg += "#"

    num_of_rows = int(len(msg) / len(key))

    arr = [[0] * len(key) for i in range(num_of_rows)]
    z = 0
    for i in range(num_of_rows):
        for j in range(len(key)):
            arr[i][j] = msg[z]
            z += 1


    for i in range(num_of_rows):
        for j in range(len(key)):
            print(arr[i][j], end=" ", flush=True)
        print()

    num_loc = get_number_location(key, m)

    cipher_text = ""

    for j in range(num_of_rows):
        for k in range(5):
              d = int(num_loc[k])
              cipher_text += arr[j][d]

    print("Cipher Text: {}".format(cipher_text))


def get_number_location(key, m):

    num_loc = ""
    for i in range(len(key) + 1):
        for j in range(len(key)):
            if m[j] == i:
                num_loc += str(j)

    return num_loc


def keyword_num_assign(key):

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    m = list(range(len(key)))

    init = 0
    for i in range(len(alpha)):
        for j in range(len(key)):
            if alpha[i] == key[j]:
                init += 1
                m[j] = init

    return m


def main():
        print("Transposition Cipher")
        print("-------------------------------")
        cipher_encryption()


if __name__ == "__main__":
    main()
