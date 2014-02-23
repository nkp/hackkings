from hackkings.models import Attachment
from hackkings.models import User
from hackkings import db
from sqlalchemy import or_
from hackkings.constants import STATES

class Project(db.Model):
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    #developers is back reffed
    state = db.Column(db.Integer, unique = False)
    proposer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.Text, unique=False)
    # proposer is back reffed
    #skills are back reffed
    #time in hours
    time_estimate = db.Column(db.Integer, unique=False)
    difficulty = db.Column(db.Integer, unique=False)
    attachments = db.relationship('Attachment', backref='project', lazy='dynamic')

    def __init__(self, name,proposer,description,time_estimate,difficulty):
        self.name = name
        self.state = STATES.PENDING
        self.proposer = proposer
        self.description = description
        self.time_estimate = time_estimate
        self.difficulty = difficulty

    @classmethod
    def create(cls, name, proposer, description, time_estimate, difficulty):
        new_project = Project( name, proposer, description, time_estimate, difficulty)
        db.session.add(new_project)
        db.session.commit()
        return new_project

    def __repr__(self):
        return '<Project %r>' % self.type

    def add_developer_by_id(self, id):
        dev = User.query.filter_by(id = id).first()
        if dev != None:
            self.add_developer(dev)

    def add_developer(self, dev):
        self.developers.append(dev)
        self.state = STATES.ONGOING
        db.session.commit()

    def remove_developer(self, id):
        dev = self.developers.query.filter_by(id = id).first()
        if dev != None:
            self.developers.remove(dev)
            if not self.developers.query.all():
                self.state = STATES.PENDING
            db.session.commit()

    @classmethod
    def find(cls, id):
        return Project.query.filter_by(id = id).first()

    def get_skills(self):
        return self.skills.all()

    def get_attachments(self):
        return self.attachments.all()

    def get_current_developers(self):
        return self.developers.all()
   
    def add_skill_id(self, skill_id):
        skill_obj = Skill.query.filter_by(id = skill_id).first()
        if skill_obj != None:
            self.add_skill(skill_obj)
        else:
            pass # Maybe it should return an error

    def add_skill(self, skill_obj):
        if self.skills.filter_by(id = skill_obj.id).first() == None:
            self.skills.append(skill_obj)
            db.session.commit()
        else:
            pass # Maybe it should return an error

    def remove_skill_id(self, skill_id):
        skill_obj = Skill.query.filter_by(id = skill_id).first()
        if skill_obj != None:
            self.remove_skill(skill_obj)
        else:
            pass # Maybe it should return an error

    def remove_skill(self, skill_obj):
        if self.skills.filter_by(id = skill_obj.id).first() != None:
            self.skills.remove(skill_obj)
            db.session.commit()
        else:
            pass # Maybe it should return an error

    @classmethod
    def get_all_pending_projects(cls):
        return Project.query.filter(cls.state == STATES.PENDING).all()

    @classmethod
    def get_all_current_projects(cls):
        return Project.query.filter(or_(cls.state == STATES.ONGOING, cls.state == STATES.PENDING)).all() # Could be made more efficient by selecting only required columns
