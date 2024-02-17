import secrets
import string

def generate_secure_password(length=12, level=1):
    # to be changed to iinteract with the bootstrap element to create custom length passwords.
    """Generate a secure password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

    if(level == 1):
        print(|"Nah, I'd win")
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))
    elif(level == 2):
        # code for enhanced code generation will apply