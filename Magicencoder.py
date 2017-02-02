import hashlib



def Credit():
    print('#############################')
    print('##                         ##')
    print('#  ***Magic Encoder v1***   #')
    print('# Script by Pentester Rekax #')
    print('##                         ##')
    print('#############################')
Credit()


parol = input("Set Password: ")

m=hashlib.md5(parol.encode('utf-8')).hexdigest()

a = (parol)
hashing = m
hash256=hashlib.sha256(hashing.encode('utf-8')).hexdigest()
#bash = hash.hexdigest()
has = hashlib.md5(hash256.encode('utf-8')).hexdigest()
print (has)
