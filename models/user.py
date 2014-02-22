from hackkings import db
from hackkings.models.project import Project
from hackkings.linkingtables import developer_project_link, skill_users_link
from hackkings.constants import STATES, ROLES

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(80), unique=False)
    avatar = db.Column(db.Text, unique=False)
    role = db.Column(db.Integer, unique=False) # If we can, limit this to the roles defined in constants
    # skills are backrefed
    bio = db.Column(db.Text, unique=False)

    projects = db.relationship('Project', secondary=developer_project_link, backref=db.backref('developers', lazy='dynamic'))
    proposals = db.relationship('Project', backref='proposer', lazy='dynamic')

    def __init__(self, username, email, name, avatar, role, bio):
        self.username = username
        self.email = email
        self.name = name
        self.avatar = avatar
        self.role = role
        self.bio = bio

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