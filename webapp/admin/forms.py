from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

class JobForm(FlaskForm):
	company = StringField('Company', validators=[DataRequired()])
	start_date = DateField(
        label='Start Date',
        format='%Y-%m-%d',
        validators = [DataRequired('please select startdate')]
    )
	end_date = DateField(
        label='End Date',
        format='%Y-%m-%d',
        validators = [DataRequired('please select startdate')]
    )
	job_title = StringField('Job Title', validators=[DataRequired()])
	description = TextAreaField('Description', validators=[DataRequired()])
	submit = SubmitField('Add Job')