from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField
from webapp.models import Company

class JobForm(FlaskForm):
	company = SelectField()

	def __init__(self, *args, **kwargs):
		self.company.kwargs['choices'] = [(item.name, item.name) for item in Company.objects.all()]
		FlaskForm.__init__(self, *args, **kwargs)

	start_date = DateField(
		label='Start Date',
		format='%Y-%m-%d',
		validators = [DataRequired('please select start date')]
	)
	end_date = DateField(
		label='End Date',
		format='%Y-%m-%d',
		validators = [DataRequired('please select end date')]
	)
	job_title = StringField('Job Title', validators=[DataRequired()])
	description = TextAreaField('Description', validators=[DataRequired()])
	achievements = TextAreaField('Achievements')
	submit = SubmitField('Add Job')

class CompanyForm(FlaskForm):
	name = StringField('Company Name', validators=[DataRequired()])
	description = StringField('Company Description')
	img_url = StringField('Company Image URL', validators=[DataRequired()])

