from webapp import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from bson.objectid import ObjectId
from datetime import datetime

@login.user_loader
def load_user(id):
	return User.objects(id=id).first()

class Post(db.EmbeddedDocument):
	oid = db.ObjectIdField(required=True, default=ObjectId,
                    unique=True, primary_key=True, sparse=True)
	title = db.StringField()
	body = db.StringField()
	post_date = db.DateTimeField(required=True, default=datetime.today(),)

class Company(db.Document):
	oid = db.ObjectIdField(required=True, default=ObjectId,
                    primary_key=True, sparse=True)
	name = db.StringField()
	description = db.StringField()
	img_url = db.StringField()
	website = db.StringField()

class Job(db.EmbeddedDocument):
	oid = db.ObjectIdField(required=True, default=ObjectId,
                    unique=True, primary_key=True, sparse=True)
	company = db.ReferenceField(Company)
	start_date = db.DateTimeField()
	end_date = db.DateTimeField()
	job_title = db.StringField()
	description = db.StringField()
	achievements = db.StringField()

class User(db.Document, UserMixin):
	username = db.StringField(required=True, unique=True)
	pwd_hash = db.StringField()
	jobs = db.ListField(db.EmbeddedDocumentField(Job))
	posts = db.ListField(db.EmbeddedDocumentField(Post))

	def to_json(self):
		return {"username": self.username,
				"pwd_hash": self.pwd_hash}

	def set_password(self, password):
		self.pwd_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pwd_hash, password)

	def add_job(self, job):
		self.jobs.append(job)

	def remove_job(self, job):
		self.jobs.remove(job)

	def post(self, post):
		self.posts.append(post)

	def remove_post(self, post):
		self.posts.remove(post)
