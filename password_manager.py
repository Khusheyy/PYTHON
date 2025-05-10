from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as keyfile:
        keyfile.write(key)

def load_key():
    file = open('key.key','rb')#were opening this file key.key in read bits mode
    key = file.read()
    file.close()
    return key

# key = Fernet.generate_key()
# keyvalue = Fernet(key)
# e_msg = keyvalue.encrypt(b"heloo this is khushi and im learning python rn , making some small and easy projects with tim!!")
# d_msg = keyvalue.decrypt(e_msg)
# print("the encrypted message : ",e_msg)
# print("the key value : ",keyvalue)
# print("the decrypted message : ",d_msg)

# master_pwd = input("What is the master password? : ")

if __name__ == "__main__":
    master_pwd = input("What is the master password? : ")
    try:
        key = load_key()
    except FileNotFoundError:
        print("Key file not found. Generating a new key...")
        write_key()
        key = load_key()

    fer = Fernet(key)
    
    
# key = load_key() 
# fer = Fernet(key)
    
def view():
    with open('passwords101.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            #here printing line also reads the invisible \n charecter , which we then solve using the rstrip()
            user, passw = data.split("|") 
            print("User: ",user,  ", Password: ",fer.decrypt(passw.encode()).decode())
            # try:
            #     user, passw = data.split("|")
            # except ValueError:
            #     print(f"Invalid format: {data}")

            

def add():
    name = input('Account name : ')
    pwd = input("Password : ")
    
    with open('passwords101.txt', 'a') as f: 
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



            

def add():
    name = input('Account name : ')
    pwd = input("Password : ")
    
    with open('passwords101.txt', 'a') as f: 
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password OR view existing password? (view/add)  , press q to quit : ").lower()
    if mode =="q":
        break
    
    if mode == "view":
        view()
    
    elif mode == "add":
        add()
    
    else:
        print("invalid mode!")
        continue

if __name__ == "__main__":
    master_pwd = input("What is the master password? : ")
    try:
        key = load_key()
    except FileNotFoundError:
        print("Key file not found. Generating a new key...")
        write_key()
        key = load_key()

    fer = Fernet(key)