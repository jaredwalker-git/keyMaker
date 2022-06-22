#keyAccess for keyMaker by Jared Walker
import numpy as np 
import string 

def isInt(str): #Custom function to check digit
    try:
        int(str)
        return True
    except ValueError:
        return False

def stringtolist(string):
    char_ls = []
    for char in string:
        char_ls.append(char)
    return char_ls

class keyAgent:
    def __init__(self):
        #PROMPT ASKS 
        print("\nkeyMaker Initialized\n")
        self.store = 'None'
        self.password = 'None'
        self.chars = stringtolist(string.ascii_letters + string.digits)
        
    def gen(self):
        generate = True
        key_gen = ''
        char_list = []
        serv = input('Enter the name of the service that you will be creating a password for:')
        user = input('Enter your username:')
        passtype = input('Would you like to make your own password or have keyMaker generate one?(gen/enter).\n')

        while generate:
            if passtype == 'enter':
                password = input('Enter your password:')
                break
            elif passtype == 'gen':
                length = input('How long would you like your password to be? Please enter an integer: ')

                while not isInt(length): #make sure a value is passed 
                    length = input('That was not a good value, please enter an integer.\nHow long would you like your password to be? Please enter an integer: ')

                req = input('Are there any characters you would like to include or that are required?(y/n): ')
            else:
                print('Invalid Response. Choose "gen" or "enter".\n')

            passlength = 0
            
            while passlength < int(length):
                key_gen = key_gen + np.random.choice(self.chars)
                passlength += 1

            if req == 'y':
                reqchar = input('What character would you like the password to include?: ')
                key_gen = list(key_gen) #turn to a list to assign the character and then reverse
                key_gen[np.random.randint(int(length))] = reqchar
                key_gen = ''.join(key_gen)
            elif req == 'n':
                pass
            else:
                print('Invalid response. Enter "y" or "n".\n')

            print("Your generated password is: " + key_gen)
            accept = input('Accept this password?(y/n):')

            if accept == 'y':
                password = key_gen
                break
            elif accept =='n':
                pass
            else:
                print('Invalid Response!')
            
        

        with open('passwords/keyAccess.txt', 'a') as f:
            f.write(serv + ':' + user + ':' + password + '\n')
  
    def access(self):
        
        with open('passwords/master.txt', 'r') as f:
            cred = f.readlines()
            masterpass = cred[1]
        
        pswd = input('Master Password: ')
        if pswd == masterpass:
            print('Success!\n')
        else:
            print('Access Denied!')
            return
            
        with open('passwords/keyAccess.txt', 'r') as f:
            for line in f:
                servname = ''
                for char in line:
                    if char == ':':
                        break
                    else:
                        servname = servname + char

                print(servname)

            serv = input('Enter the name of the service:')
            for line in f:
                if serv in line:
                    print(line)
                    break
                else:
                    continue

    def del():
        choice = input('Which password would you like to delete?:')

        with open('passwords/keyAccess.txt', 'r') as f:
            content = f.readlines()
        
        for i in len(content):
            #if content[i] is choice then content[i] == ''