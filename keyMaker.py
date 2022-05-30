#keyMaker: A keygen/keystore service
#Jared Walker 5/17/2022

from genericpath import exists
import argparse
import keyAgent

#ACCESS MUST ASK FOR STORAGE FILE, MAYBE REQUIRED PASSWORD ASWELL // STATEMENT CHECKING FOR PASSWORD FILE IF NOT EXISTING, NEW USER PROMPT

#ACCESS MODE ACCESSES LIST OF DICTIONARIES WITH NAME OF SERVICE, USERNAME AND PASSWORD COMBO
if __name__ == '__main__':
    keyMaker = keyAgent.keyAgent()

    #PARSER TO TAKE IN ARGUMENTS FOR MODE// KEYGEN MODE OR ACCESS MODE
    parser = argparse.ArgumentParser(description="Generate and store keys")
    parser.add_argument('mode', help='Enter mode either "gen" or "access"')
    args = parser.parse_args()
    #CHECK FOR INITIAL BOOT // do this with file holding password? // how to make python script password protected
    if exists('passwords/master.txt'):
        pass
    else:
        print("Welcome to KeyMaker! Thank you for using Jared's dope service for keeping your passwords safe!")
        usr = input('Please enter your account name for keyMaker:')
        masterp = input('Please enter a master password for keymaker. THIS WILL BE THE ONLY PASSWORD YOU MUST REMEMBER!\nMaster Password:')
        masterp2 = input('Please re-enter the password.')

        while not (masterp == masterp2):
            print('Passwords did not match, try again.')
            masterp = input('Please enter a password for keymaker. THIS WILL BE THE ONLY PASSWORD YOU MUST REMEMBER!')
            masterp2 = input('Please re-enter the password.')

        with open('passwords/master.txt', 'a') as f:
            f.write(usr + '\n')
            f.write(masterp)
            

        print('Password saved!')

    with open('passwords/master.txt', 'r') as f:
        content = f.readlines()
        print('Hello ' + content[0]) #print username

    #initial argparse action
    if args.mode == 'gen':
        keyMaker.gen()
    elif args.mode == 'access':
        keyMaker.access()
    else:
        print('Invalid mode.')

    while True:
        #KEYGEN MODE WILL ASK FOR ENTRY INFO
        func = input('Would you like to continue using keyMaker?\nEnter one of the following modes or q to quit. - (gen/access/q):')
        if func == 'gen':
            keyMaker.gen()
        elif func == 'access':
            keyMaker.access()
        elif func == 'q': 
            break
        else:
            print('Invalid selection.')