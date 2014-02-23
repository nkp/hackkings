import bcrypt
from hackkings import BCRYPT_WORK_FACTOR

def hash_password(plain_password, salt=None):
    if isinstance(plain_password, unicode):
        plain_password = plain_password.encode('u8')
    if not salt:
        salt = bcrypt.gensalt(BCRYPT_WORK_FACTOR)
    elif isinstance(salt, unicode):
        salt = salt.encode('u8')
    return bcrypt.hashpw(plain_password, salt)


