from hackkings import db
from hackkings.models.role import Role
from hackkings.linkingtables import developer_project_link, skill_users_link

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(80), unique=False)
    avatar = db.Column(db.Text, unique=False)
    role = db.Column(db.Integer, db.ForeignKey('role.id'))
    # skills are backrefed
    bio = db.Column(db.Text, unique=False)

    projects = db.relationship('Project', secondary=developer_project_link, backref=db.backref('developers', lazy='dynamic'))
    proposals = db.relationship('Project', backref='proposer', lazy='dynamic')

    def __init__(self, username, email, name, avatar, role, skills, interests):
        self.username = username
        self.email = email
        self.name = name
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.username

    def get_completed_proposals():
        pass

    def get_ongoing_proposals():
        pass

    def get_pending_proposals():

        pass
    def get_ongoing_projects():

        pass
    def get_completed_projects():
        pass