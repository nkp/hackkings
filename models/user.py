from hackkings import db
from hackkings.models import Skill
from hackkings.linkingtables import developer_project_link, skill_users_link
from hackkings.constants import STATES, ROLES, BCRYPT_HASH_LENGTH 
from hackkings.utils import hash_password, check_password
from flask_login import UserMixin
from sqlalchemy import or_
from datetime import datetime, timedelta
from threading import Thread
from werkzeug.security import safe_str_cmp
from hackkings.utils import CodeAcademyQueue
from datetime import datetime

DAY_DELTA = timedelta(1)

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    _password = db.Column(db.String(BCRYPT_HASH_LENGTH))
    name = db.Column(db.String(80), unique=False)
    avatar = db.Column(db.Text, unique=False)
    role = db.Column(db.Integer, unique=False) # If we can, limit this to the roles defined in constants
    # skills are backrefed
    bio = db.Column(db.Text, unique=False)
    code_academy_username = db.Column(db.String(30), unique=True)
    code_academy_fetch_time = db.Column(db.DateTime, unique=False, default=lambda ctx: datetime.utcnow() - DAY_DELTA*2)
    _code_academy_badges = db.Column(db.Text, unique=False)

    projects = db.relationship('Project', secondary=developer_project_link, lazy='dynamic', backref=db.backref('developers', lazy='dynamic'))
    proposals = db.relationship('Project', backref='proposer', lazy='dynamic')
    messages_sent = db.relationship('Message', backref='sender', lazy='dynamic')

    def __init__(self, username, email, password, role, name, avatar, bio):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.avatar = avatar
        self.role = role
        self.bio = bio


    def set_username(self, username):
        self.username = username
        db.session.commit()

    def set_email(self, email):
        self.email = email
        db.session.commit()

    def set_role(self, role):
        self.role = role
        db.session.commit()

    def set_code_academy_username(self, code_academy_username):
        self.code_academy_username = code_academy_username
        db.session.commit()
        self.get_code_academy_badges()

    def set_code_academy_badges(self, html):
        self._code_academy_badges = html
        self.code_academy_fetch_time = datetime.utcnow()
        db.session.commit()
        print self._code_academy_badges
        
    def get_code_academy_badges(self):
        print 'Getting code' # Was used, now does nothing
        #if datetime.utcnow() > self.code_academy_fetch_time - DAY_DELTA:
            #print 'After the delta'
            #CodeAcademyQueue.put(self)
            #self.code_academy_fetch_time = datetime.utcnow()
            #db.session.commit()
        return self._code_academy_badges

    @classmethod
    def create(cls, username, email, password, role):
        new_user = User(username, email, password, role, None, "/static/uploads/default.png", None)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    def get_password(self):
        return self._password

    def set_password(self, plain_password):
        self._password = hash_password(plain_password)
        db.session.commit()

    password = property(fget=get_password, fset=set_password)

    def check_password(self, plain_password):
        return check_password(self.password, plain_password)
        password_hash = hash_password(plain_password, self.password)
        return safe_str_cmp(password_hash, self.password)

    def __repr__(self):
        return '<User %r>' % self.username

    def get_completed_proposals(self):
        return self.proposals.filter_by(state = STATES.COMPLETED).all()

    def get_ongoing_proposals(self):
        return self.proposals.filter_by(state = STATES.ONGOING).all()

    def get_pending_proposals(self):
        return self.proposals.filter_by(state = STATES.PENDING).all()

    def get_ongoing_projects(self):
        return self.projects.filter_by(state = STATES.ONGOING).all()

    def get_completed_projects(self):
        return self.projects.filter_by(state = STATES.COMPLETED).all()

    @classmethod
    def find(cls, id):
        return User.query.filter_by(id = id).first()

    @classmethod
    def find_by_email(cls, email):
        return User.query.filter_by(email = email).first()

    @classmethod
    def find_by_username(cls, username):
        return User.query.filter_by(username = username).first()

    @classmethod
    def find_by_identifier(cls, identifier):
        return User.query.filter(or_(cls.email == identifier, 
                                     cls.username == identifier)).first()

    def add_skill_id(self, skill_id):
        skill_obj = Skill.query.filter_by(id = skill_id).first()
        if skill_obj != None:
            if self.skills.filter_by(id = skill_obj.id).first() == None:
                self.skills.append(skill_obj)
                db.session.commit()
        else:
            pass # Maybe it should return an error

    def add_skill(self, skill_obj):
        if self.skills.filter_by(id = skill_obj.id).first() == None:
            self.skills.append(skill_obj)
            db.session.commit()
        else:
            pass # Maybe it should return an error

    def get_skills(self):
        return self.skills.all()

    def remove_skill_id(self, skill_id):
        skill_obj = Skill.query.filter_by(id = skill_id).first()
        if skill_obj != None:
            if self.skills.filter_by(id = skill_obj.id).first() != None:
                self.skills.remove(skill_obj)
                db.session.commit()
        else:
            pass # Maybe it should return an error

    def remove_skill(self, skill_obj):
        if self.skills.filter_by(id = skill_obj.id).first() != None:
            self.skills.remove(skill_obj)
            db.session.commit()
        else:
            pass # Maybe it should return an error

    def is_proposer(self):
        return self.role == ROLES.PROPOSER

    def is_developer(self):
        return self.role == ROLES.DEVELOPER

    def set_bio(self, bio):
        self.bio = bio
        db.session.commit()

    def set_name(self, name):
        self.name = name
        db.session.commit()

    def set_avatar(self, link):
        self.avatar = link
        db.session.commit()
