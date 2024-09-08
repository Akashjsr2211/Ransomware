import os
from cryptography.fernet import Fernet

cwd= os.getcwd()
file_list=[]
for root,dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith('.txt'):
            file_list.append(os.path.join(root,file))



def decryption(file_list):
    with open('secret.key','rb') as f:
        decryption_key = f.read()
    fernet = Fernet(decryption_key)
    for file in file_list:
        with open(file,'rb') as f:
            encrypted_data=f.read()
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        with open(file,'w') as f:
            f.write(decrypted_data)
        
print("//////////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////////")
print("////////// Successfully Decrypted all your data !! ////////")
print("//////////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////////")
print("/////////////////////////////////////////////////////////")
decryption(file_list)