from webapp import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
	return User.objects(id=id).first()

class Job(db.EmbeddedDocument):
	company = db.StringField()
	start_date = db.DateTimeField()
	end_date = db.DateTimeField()
	job_title = db.StringField()
	description = db.StringField()

class User(db.Document, UserMixin):
	username = db.StringField(required=True, unique=True)
	pwd_hash = db.StringField()
	jobs = db.ListField(db.EmbeddedDocumentField(Job))

	def to_json(self):
		return {"username": self.username,
				"pwd_hash": self.pwd_hash}

	def set_password(self, password):
		self.pwd_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pwd_hash, password)

