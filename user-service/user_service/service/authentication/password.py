import re

from password_strength import PasswordPolicy
from passlib.context import CryptContext


PASSWORD_SCHEMES = ["bcrypt"]
MIN_PASSWORD_LENGTH = 10
crypt_context = CryptContext(schemes=PASSWORD_SCHEMES)

def hash_password(password):
    hashed_password = crypt_context.hash(password)
    return hashed_password


def verify_password(password, password_hash):
    return crypt_context.verify(password, password_hash)


def password_hash_is_deprecated(password_hash):
    return crypt_context.needs_update(password_hash)


def check_password_strength_default(password):
    if len(password) < MIN_PASSWORD_LENGTH:
        raise PasswordStrengthError('Password must be at least {} characters'.format(MIN_PASSWORD_LENGTH))

    num_lowercase = len(re.findall('[a-z]', password))
    num_uppercase = len(re.findall('[A-Z]', password))
    num_digits = len(re.findall('[0-9]', password))
    num_special = len(re.findall(r"""[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]""", password))

    counts = [num_lowercase, num_uppercase, num_digits, num_special]
    num_passed = len([count for count in counts if count >= 1])
    if not num_passed >= 3:
        message = ('Password must have at least 3 of these character types: '
                   'lowercase, uppercase, digits, special characters')
        raise PasswordStrengthError(message)

