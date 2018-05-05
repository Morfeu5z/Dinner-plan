from my_app import db

class Role(db.Model):
    idRole = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)

    #users = db.relationship('User', backref='role')
    def __repr__(self):
        return '<ROLE %r>' % self.name


class User(db.Model):
    idUser = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.String(200))
    name = db.Column(db.String(50))
    surname = db.Column(db.String(100))
    #idRole = db.Column(db.Integer, db.ForeignKey('roles.idRole'))

    def __init__(self, email, name, surname):
        self.name = name
        self.email = email
        self.surname = surname

    def __repr__(self):
        return '<USER %r>' % self.email

