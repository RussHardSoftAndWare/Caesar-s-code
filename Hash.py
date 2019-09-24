### Hash

### Imports
import hashlib

### Vars
passwd = input("Введите пароль: ")

### Fucntions
def ConvertToHash(passwd):
    passwd = bytes(passwd, encoding="utf-8")
    sha = hashlib.sha1(passwd).hexdigest()
    print(sha)

### Call
ConvertToHash(passwd)
