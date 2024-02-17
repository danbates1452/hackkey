import secrets
import string

def generate_secure_password(length=12):
    # to be changed to iinteract with the bootstrap element to create custom length passwords.
    """Generate a secure password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def generate_secure_password_tier2(length):
    # to be changed to iinteract with the bootstrap elements to create custom length passwords.
    """Generate a secure password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password