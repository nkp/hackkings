class Attachment(db.Model):
    __tablename__ = 'attachment'
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.Text)
    
    def __init__(self, link):
        self.link = link

    def __repr__(self):
        return '<Link %r>' % self.link
