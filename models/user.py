from hackkings import db
from hackkings.models import Skill
from hackkings.linkingtables import developer_project_link, skill_users_link
from hackkings.constants import STATES, ROLES, BCRYPT_HASH_LENGTH 
from hackkings.utils import hash_password, check_password
from flask_login import UserMixin
from sqlalchemy import or_

from werkzeug.security import safe_str_cmp
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

    @classmethod
    def create(cls, username, email, password, role):
        new_user = User(username, email, password, role, None, None, None)
        db.session.add(new_user)
        db.session.commit()
    
    def get_password(self):
        return self._password

    def set_password(self, plain_password):
        self._password = hash_password(plain_password)

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
        print self.projects.filter_by(state = STATES.ONGOING).all()
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
        self.bio = bio;

    def set_name(self, name):
        self.name = name;
