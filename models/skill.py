from hackkings import db
from hackkings.models.project import Project
from hackkings.models.user import User
from hackkings.linkingtables import skill_projects_link, skill_users_link

class Skill(db.Model):
    __tablename__ = "skill"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    projects = db.relationship('Project', secondary=skill_projects_link, backref=db.backref('skills', lazy='dynamic'))
    users = db.relationship('User', secondary=skill_users_link, backref=db.backref('skills', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Skill %r>' % self.name