import sys
import hashlib


def bitExtracted(number, k, p):
    return ((1 << k) - 1) & (number >> (p - 1))


def FileCryptor(crypt_or_decrypt, file, key):
    try:
        f = open(file, mode='r', encoding='utf-8')
        file_content = f.read()
        if crypt_or_decrypt == "crypt":
            out = open("C:\\Users\\user\\Desktop\\test\\crypt", mode='w', encoding='utf-8')
            i = 0
            for c in file_content:
                offset = key[i % len(key)]
                if (ord(c) + ord(offset)) > 255:
                    final = bitExtracted(ord(c) + ord(offset), 8, 1)
                else:
                    final = ord(c) + ord(offset)
                new = chr(final)
                out.write(new)
                i += 1
        elif crypt_or_decrypt == "decrypt":
            out = open("C:\\Users\\user\\Desktop\\test\\decrypt", mode='w', encoding='utf-8')
            i = 0
            for c in file_content:
                offset = key[i % len(key)]
                if (ord(c) - ord(offset)) > 255:
                    final = bitExtracted(ord(c) - ord(offset), 8, 1)
                else:
                    final = ord(c) - ord(offset)
                new = chr(final)
                i += 1
                out.write(new)

    finally:
        f.close()
        out.close()


if __name__ == '__main__':
    # print("My Python Project")
    command = str(sys.argv[1])
    from_file = str(sys.argv[2])
    password = str(sys.argv[3])
    print(FileCryptor(command, from_file, password))

    # check if the original file and the decrypted one are the same
    path = r'C:\Users\user\Desktop\test\decrypt'
    with open(path, 'rb') as opened_file:
        content = opened_file.read()
        md5 = hashlib.md5()
        md5.update(content)
    path1 = r'C:\Users\user\Desktop\test\proiect.txt'
    with open(path1, 'rb') as opened_file1:
        content1 = opened_file1.read()
        md5new = hashlib.md5()
        md5new.update(content1)
    if md5.hexdigest() == md5new.hexdigest():
        print("the encryption and decryption worked")
