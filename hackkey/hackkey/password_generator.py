import secrets
import string

def generate_secure_password(length=12, level=1):
    if(level == 1):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        return password
    elif(level == 2):
        return ""
        # code for enhanced code generation will apply