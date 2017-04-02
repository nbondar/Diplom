from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    passw = db.Column(db.String(32))
    name = db.Column(db.String(32))
    surname = db.Column(db.String(32))
    phonenumber = db.Column(db.Integer)
    namespaces = db.relationship('Namespace', backref = 'user', lazy = 'dynamic')
    pay = db.relationship('Payment', backref = 'user', lazy = 'dynamic')


    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Namespace(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)       
    name = db.Column(db.String(64))
    count = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime)
    deployments = db.relationship('Deployment', backref = 'namespace', lazy = 'dynamic')


    def __repr__(self):
        return '<Namespace %r>' % (self.name)


class Deployment(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    name = db.Column(db.String(64))
    namespace_id = db.Column(db.Integer, db.ForeignKey('namespace.id'))
    timestamp = db.Column(db.DateTime)
    pods = db.relationship('Pods', backref = 'deployment', lazy = 'dynamic')


    def __repr__(self):
        return '<Deployment %r>' % (self.name)

class Pods(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True) 
    name = db.Column(db.String(50))
    deployment_id = db.Column(db.Integer, db.ForeignKey('deployment.id'))
    replicas = db.Column(db.Integer)
    size =  db.Column(db.Float)
    status =  db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)


    def __repr__(self):
        return '<Pods %r>' % (self.name)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)  
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    period_begin = db.Column(db.DateTime)
    period_end = db.Column(db.DateTime)
    price = db.Column(db.Float)


    def __repr__(self):
        return '<Payment %r>' % (self.period_begin, self.period_end)






