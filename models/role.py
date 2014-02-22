class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Role %r>' % self.type