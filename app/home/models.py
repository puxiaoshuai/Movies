from app import db
class Role(db.Model):
    __table__name='roles'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(64),unique=True,index=True)
    users=db.relationship("User",backref='role')
    def __repr__(self):
        return "Role is %s " %self.name
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username=db.Column(db.String(64),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    def __repr__(self):
        return "User:%s"% self.username