from hackkings import db

class Project(db.Model):
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    #developers
    #completed
    #state
    #proposer
    #description
    #skills_needed
    #time_estimate
    #difficulty
    #attachments

    def __init__(self, name,developers,completed,state,proposer,description,skills_needed,time_estimate,difficulty,attachments):
        self.name = name
        self.developers = developers
        self.completed = completed
        self.state = state
        self.proposer = proposer
        self.description = description
        self.skills_needed = skills_needed
        self.time_estimate = time_estimate
        self.difficulty = difficulty
        self.attachments = attachments

    def __repr__(self):
        return '<Project %r>' % self.type