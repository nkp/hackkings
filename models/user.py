from models.role import Role

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(80), unique=False)
    role = db.Column(db.Integer, db.ForeignKey('role.id'))
    # currentproject = db. # Many to many

    def __init__(self, username, email, name, role):
        self.username = username
        self.email = email
        self.name = name
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.username