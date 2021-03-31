from webapp import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
	return User.objects(id=id).first()

class User(db.Document, UserMixin):
	username = db.StringField()
	pwd_hash = db.StringField()

	def to_json(self):
		return {"username": self.username,
				"pwd_hash": self.pwd_hash}

	def set_password(self, password):
		self.pwd_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pwd_hash, password)