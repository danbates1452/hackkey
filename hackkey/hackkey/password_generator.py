import secrets
import string

def generate_secure_password(level=1, length=10):
    if(level == 1):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        return password
    elif(level == 2):
        return ""
        # code for enhanced code generation will apply

def pass_credentials_to_database(usrID, username, password):
    # pass to DB here