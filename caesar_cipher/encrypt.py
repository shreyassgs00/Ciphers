#To encrypt strings using Caesar ciphers (shift ciphers)

a = input('Enter a string to encrypt using Caesar cipher: ')
s = int(input('Enter the shift pattern: '))

if s > 25:
    print('Shift pattern is not valid as the number is greater than or equal to 26')
else:
    ans = ''
    for i in range(0, len(a)):
        if ord(a[i]) >= 97 and ord(a[i]) <= 122:
            ans = ans + chr(ord(a[i])-32+s)
        elif ord(a[i]) >= 65 and ord(a[i]) <= 90:
            ans = ans + chr(ord(a[i])+32+s)
        else:
            ans = ans + a[i]
    encrypt_file = open('encrypted.txt','w')
    encrypt_file.write(ans)
