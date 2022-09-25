import hashlib
from time import sleep

flag = 0
counter = 0

number_hash = input("Enter md5 hash : ")

# try:
#     import codecs
#     with codecs.open('hash_list.txt', 'r', encoding='utf-8',
#                  errors='ignore') as pass_file:
#        print("ok")
# except:
#     print("No File Found")
#     quit()
with open('hash_list.txt', 'r') as f:
    for word in f:
        a = word
        b = a.split()
        c = b[2] 
        e = b[0]

        if c == number_hash:
            print("decoded : ")
            print(e)
            flag = 1
            sleep(10)
            break

# passbaba = pass_file


# if flag == 0 :
#     print("not in data base")
#     sleep(5)