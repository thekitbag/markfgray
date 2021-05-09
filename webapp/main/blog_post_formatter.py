class BlogPost(object):
	def __init__(self, post):
		self.post = post
		self.title = post.title
		self.body = post.body
		self.oid = post.oid
		self.post_date = post.post_date
		self.format_content()

	def format_content(self):
		self.paragraphs = self.body.split('\r')
