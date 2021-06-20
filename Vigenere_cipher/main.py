import os
import sys

def check_key(key):
    count = 0
    for i in key:
        if i.isalpha():
            continue
        else:
            count += 1
    if count>0:
        return False
    else:
        return True

def encrypt_key(key):
    string1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_list = []
    for i in range(0, len(key)):
        for j in range(0, len(string1)):
            if key[i] == string1[j]:
                key_list.append(j+1)
            elif key[i] == string1[j].lower(): 
                key_list.append(j+1)
    return key_list

def encrypt_key_string(string, key):
    key_list = encrypt_key(key)
    new_list = []
    new_list_length = len(string)
    for i in range(0, new_list_length):
        if i < 5:
            new_list.append(key_list[i])
        else:
            new_list.append(key_list[i%5])
    return new_list

def encrypt_string(string, key):
    key_list = encrypt_key(key)
    string_encrypted_list = encrypt_key_string(string, key)
    encrypted_string = ''
    for i in range(0, len(string)):
        if ord(string[i]) >= 65 and ord(string[i]) < 91:
            encrypted_string += chr(((ord(string[i])%26)+string_encrypted_list[i]+ord('A')))
        elif ord(string[i]) >= 97 and ord(string[i]) < 123:
            encrypted_string += chr(((ord(string[i])%26)+string_encrypted_list[i]+ord('a')))
        else:
            encrypted_string += string[i]
    return encrypted_string

if __name__ == '__main__':
    string1 = input("Enter a string: ")
    key = input('Enter the key: ')
    if check_key(key):
        encrypted_string = encrypt_string(string1,key)
        print(encrypted_string)
    else:
        print('Key value not a string.')
        sys.exit()