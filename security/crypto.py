from cryptography.fernet import Fernet

key=Fernet.generate_key()
cipher=Fernet(key)

def encrypt(x:str):
 return cipher.encrypt(x.encode()).decode()

def decrypt(x:str):
 return cipher.decrypt(x.encode()).decode()
