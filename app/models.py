from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    '''Base de dados para armazenar dados básicos dos usuários'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    firstname = db.Column(db.String(64))
    fullname = db.Column(db.String(128))

    def __repr__(self):
        return f"<username: {self.username}>"


class Hosts(db.Model):
    '''Tabela que armazena os hosts'''
    id = db.Column(db.Integer, primary_key=True)
    host_name = db.Column(db.String(64), unique=True)
    host_id = db.Column(db.String(32))
    host_distro = db.Column(db.String(24))
    host_release = db.Column(db.String(32))
    host_kernel = db.Column(db.String(45))
    host_version = db.Column(db.String(6))
    host_ip = db.Column(db.String(15))
    updates = db.relationship('Updates', backref='tipo', lazy=True)

    def __repr__(self):
        return f"<host: {self.host_name}>"


class Updates(db.Model):
    """Tabela que armazena as atualizações"""
    id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, db.ForeignKey('hosts.id'), nullable=False)
    update = db.Column(db.String(128), unique=True)


    def __repr__(self):
        return f"<update: {self.update}>"

