import base64
import os
from cryptography import fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sys

mysalt = b'q\xeb\xf2X\x0f\xac\x06\xc4\x07\x86F\xe3\xc8\xfc\x96\xe0'
def encrypt(Text, Passworld):
    print("Encrypting")
    
    kdf = PBKDF2HMAC (
        algorithm=hashes.SHA256,
        length=32,
        salt=mysalt,
        iterations=100000,
        backend=default_backend()
    )
    enpswd = str(Passworld).encode()
    key = base64.urlsafe_b64encode(kdf.derive(enpswd))
    
    fkey = fernet.Fernet(key)
    iText = str(Text)
    output = fkey.encrypt(bytes(str(iText), 'utf-8'))
    os.system('cls')
    out= str(output.decode("utf-8"))
    os.system("echo "+out+'|clip')
    print(str(output.decode("utf-8")))
    input()
    

def decrypt(Text, Passworld):
    print("Decrypting")
    
    kdf = PBKDF2HMAC (
        algorithm=hashes.SHA256,
        length=32,
        salt=mysalt,
        iterations=100000,
        backend=default_backend()
    )
    enpswd = str(Passworld).encode()
    key = base64.urlsafe_b64encode(kdf.derive(enpswd))
    
    fkey = fernet.Fernet(key)
    iText = str(Text)
    output = fkey.decrypt(bytes(str(iText), 'utf-8'))
    
    os.system('cls')
    out= str(output.decode("utf-8"))
    os.system("echo "+out+'|clip')
    print(str(output.decode("utf-8")))
    input()
    
    
    
if len(sys.argv) == 2:
    if(sys.argv[1] == "-h"):
        print("usage: -d / -e [Encrypted text] [Passworld]")
        
if len(sys.argv) == 4 :
    print("--PROCESSING--")
    
    EncText = sys.argv[2]
    Passworld = sys.argv[3]
    
    if sys.argv[1]=="-d":
        print("Decryption mode")
        decrypt(EncText, Passworld)
        
        
    if sys.argv[1]=="-e":
        print("Encryption mode")
        encrypt(EncText, Passworld)
    
    else:
        print("--ERROR: No valid mode--")
        exit(1)    
    
    
if len(sys.argv) == 1 :
    Mode = input("Mode [e]/[d] :")
    Input = input("Enter Text: ")
    Pass = input("Enter passworld: ")
    if Mode == "e":
        print("Encryption mode")
        encrypt(Input,Pass)
        
    if Mode == "d":
        print("Decryption mode")
        decrypt(Input,Pass)
        