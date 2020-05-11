
from cryptography.fernet import Fernet
import os, hashlib, json, sys

def create_user(privKey, pubKey):
    proceed = False
    while proceed == False:
        name = input("Enter user name...\n")
        userinput = input("You have entered {}. Is this correct? (y/n)\n".format(name))
        if userinput == 'y':
            proceed = True

    print("Generating user key...")
    userKey = Fernet.generate_key()
    if input("\nDo you want to create a file to save this key? (y/n)\n") == 'y':
        fileName = input("Enter name for file...\n")
        with open(fileName + '.txt', 'w') as keyfile:
            keyfile.write(str(userKey))
        print("text file created {}... it is a good idea to encrypt this file for additional security \n".format(fileName + '.txt'))

    while input("Have you copied this somewhere safe? (y/n)\n") != 'y':
        print('You reaaaallllly should...')

    myPassword = input("Enter password for user {}...\n".format(name))
    print("User {} being created...".format(name))
    salt = os.urandom(32)
    type(salt)
    passKey = password_hash(userKey, salt, myPassword)
    json_dict = { "name": name, "passKey": str(passKey), "salt": str(salt), "privKey": privKey,"pubKey": pubKey }
    print(json.dumps(json_dict))
    encryptor = Fernet(userKey)
    encrypted = encryptor.encrypt(bytes(json.dumps(json_dict), "utf-8"))
    with open('data_file.json', 'w') as fout:
        fout.write(str(encrypted))
    return userKey


def password_hash(key, salt, password):
    key = hashlib.pbkdf2_hmac('sha256', (password + str(key)).encode('utf-8'), salt, 100000)
    return key



def password_verify(password, salt, json):
    salt = passDict

def access_user_keys():
    name = input("Enter saved name...\n")
    userKey = b'EfKlCz1cbhaHlmCy3BRReJQNWEMrBuamxM4p42zMamI='.decode('utf-8')
    #password = password()
    with open("data_file.json", "r") as fin:
        encrypted = Fernet(fin.read())
        decrypted = userKey.decrypt(encrypted)




access_user_keys()

#print(create_user(7, 5))

sys.exit()



x =  '''{ "organization":"GeeksForGeeks",  
        "city":"Noida",  
        "country":"India"}''' 
  
# python object to be appended 
y = {"pin":110096} 
  
# parsing JSON string: 
z = json.loads(x) 
   
# appending the data 
z.update(y) 
  
# the result is a JSON string: 
print(json.dumps(z)) 

y = { 'name': 'myname', 'hash':12345}

with open('data_file.json', 'r') as fin:
    jdata = json.load(fin)
    if y['name'] not in jdata:
        jdata.update(y)
        print(json.dumps(jdata))
