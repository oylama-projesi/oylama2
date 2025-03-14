from flask_wtf import FlaskForm
from wtforms import DateTimeLocalField, StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class OylamaForm(FlaskForm):
    question = StringField('Question', validators=[DataRequired(), Length(max=100)])
    options = TextAreaField('Options', validators=[DataRequired(), Length(max=500)])
    group_id = SelectField('Group', coerce=int, validators=[DataRequired()])
    end_time = DateTimeLocalField('End Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit = SubmitField('Create Poll')

class GroupForm(FlaskForm):
    name = StringField('Group Name', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Create Group')