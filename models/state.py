class State(db.Model):
    __tablename__ = "state"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    projects = db.relationship('Project', backref='state', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<State %r>' % self.name