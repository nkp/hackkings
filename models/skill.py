class Skill(db.Model):
    __tablename__ = "skill"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    users = db.relationship('User', backref='skill', lazy='dynamic')
    projects = db.relationship('Project', backref='skill', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Skill %r>' % self.name