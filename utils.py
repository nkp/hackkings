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
        print 'User got! ' + str(user)
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
                #print achievements
                user.set_code_academy_badges(str(achievements))
        except Exception as e:
            print e
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

def pretty_date(dt, default=None):
    """
    Returns string representing "time since" e.g.
    3 days ago, 5 hours ago etc.
    Ref: https://bitbucket.org/danjac/newsmeme/src/a281babb9ca3/newsmeme/
    """
    if default is None:
        default = 'just now'
    
    now = datetime.utcnow()
    diff = now - dt

    periods = (
        (diff.days / 365, 'year', 'years'),
        (diff.days / 30, 'month', 'months'),
        (diff.days / 7, 'week', 'weeks'),
        (diff.days, 'day', 'days'),
        (diff.seconds / 3600, 'hour', 'hours'),
        (diff.seconds / 60, 'minute', 'minutes'),
        (diff.seconds, 'second', 'seconds'),
    )

    for period, singular, plural in periods:
        if not period:
            continue
        if period == 1:
            return u'%d %s ago' % (period, singular)
        else:
            return u'%d %s ago' % (period, plural)

    return default
