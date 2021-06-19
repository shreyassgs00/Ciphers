#To decrypt the strings in encrypt.txt and write them to decrypt.txt

to_decrypt_file = open('encrypted.txt','r')
decrypt_file = open('decrypted.txt','w')
s = int(input('Enter the shift pattern to decrypt: '))

encrypted_lines = to_decrypt_file.readlines()
for a in encrypted_lines:
    ans = ''
    for i in range(0, len(a)):
        if ord(a[i]) >= 97 and ord(a[i]) <= 122:
            ans = ans + chr(ord(a[i])-32-s)
        elif ord(a[i]) >= 65 and ord(a[i]) <= 90:
            ans = ans + chr(ord(a[i])+32-s)
        else:
            ans = ans + a[i]
    decrypt_file.write(ans)
