#import bcrypt
#from hackkings.constants import BCRYPT_WORK_FACTOR
from werkzeug.security import generate_password_hash, check_password_hash
from urllib2 import urlopen, Request
from bs4 import BeautifulSoup
from datetime import datetime

from Queue import Queue
from threading import Thread, Lock

CodeAcademyQueue = Queue()
thread_pool = []
thread_lock = Lock()

def code_academy_worker(q, lock):
    while 1:
        user = q.get()
        try:
            name = user.code_academy_username
            url = 'http://codeacademy.com/users/%s/achievements' % name
            req = Request(url, headers={'User-Agent' : 'Mozilla Firefox 23'})
            page = urlopen(req)
            content = page.read()
            page.close()
            soup = BeautifulSoup(content)
            achievements = soup.find(id='userAchievements')
            with lock:
                user._code_academy_badges = str(achievements)
                user.code_academy_fetch_time = datetime.utcnow()
        except Exception:
            q.put(user)
        finally:
            q.task_done()

for i in xrange(2):
    t = Thread(target=code_academy_worker, args=(CodeAcademyQueue,thread_lock))
    t.daemon = True
    thread_pool.append(t)
    t.start()


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


