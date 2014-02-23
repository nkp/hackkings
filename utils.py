#import bcrypt
#from hackkings.constants import BCRYPT_WORK_FACTOR
from werkzeug.security import generate_password_hash, check_password_hash

def check_password(password_hash, plain_password):
    return check_password_hash(password_hash, plain_password)

def hash_password(plain_password, salt=None):
    return generate_password_hash(plain_password)
    if isinstance(plain_password, unicode):
        plain_password = plain_password.encode('u8')
    if not salt:
        salt = bcrypt.gensalt(BCRYPT_WORK_FACTOR)
    elif isinstance(salt, unicode):
        salt = salt.encode('u8')
    return bcrypt.hashpw(plain_password, salt)


