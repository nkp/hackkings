from hackkings import db
from hackkings.models import Skill
from hackkings.linkingtables import developer_project_link, skill_users_link
from hackkings.constants import STATES, ROLES, BCRYPT_HASH_LENGTH 
from hackkings.utils import hash_password
from flask_login import UserMixin

from werkzeug.security import safe_str_cmp
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    _password = db.Column(db.String(BCRYPT_HASH_LENGTH))
    name = db.Column(db.String(80), unique=False)
    avatar = db.Column(db.Text, unique=False)
    role = db.Column(db.Integer, unique=False) # If we can, limit this to the roles defined in constants
    # skills are backrefed
    bio = db.Column(db.Text, unique=False)

    projects = db.relationship('Project', secondary=developer_project_link, backref=db.backref('developers', lazy='dynamic'))
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
        password_hash = hash_password(plain_password, self.password)
        return safe_str_cmp(password_hash, self.password)

    def __repr__(self):
        return '<User %r>' % self.username

    def get_completed_proposals(self):
        return self.proposals.query.filter_by(state = STATES.COMPLETED).all()

    def get_ongoing_proposals(self):
        return self.proposals.query.filter_by(state = STATES.ONGOING).all()

    def get_pending_proposals(self):
        return self.proposals.query.filter_by(state = STATES.PENDING).all()

    def get_ongoing_projects(self):
        return self.projects.query.filter_by(state = STATES.ONGOING).all()

    def get_completed_projects(self):
        return self.projects.query.filter_by(state = STATES.COMPLETED).all()
 
    def find(self, id):
        return User.filter_by(id = id).first()

    def add_skill_id(self, skill_id):
        skill_obj = Skill.query.filter_by(id = skill_id).first()
        if skill_obj != None:
            if self.skills.query.filter_by(id = skill_obj.id).first() == None:
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
        return self.skills.query.all()

    def remove_skill_id(self, skill_id):
        skill_obj = Skill.query.filter_by(id = skill_id).first()
        if skill_obj != None:
            if self.skills.query.filter_by(id = skill_obj.id).first() != None:
                self.skills.remove(skill_obj)
                db.session.commit()
        else:
            pass # Maybe it should return an error

    def remove_skill(self, skill_obj):
        if self.skills.query.filter_by(id = skill_obj.id).first() != None:
            self.skills.remove(skill_obj)
            db.session.commit()
        else:
            pass # Maybe it should return an error
