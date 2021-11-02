passwords = {}

def decision():
    initial = input('What would you like to do: ')
    if initial.lower() == 'add password':
        add_password()

def add_password():
    key_add = input('Enter what the password is for: ')
    # if key_add in passwords.keys():
    #     print('Password for this already exists. Try edit.')
    #     decision()
    pw_add = input('Enter the password: ')
    pw_add_lc = pw_add.lower()
    key_add_lc = key_add.lower()
    passwords.update({key_add_lc: pw_add_lc})

decision()