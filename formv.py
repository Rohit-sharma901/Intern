from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class UserForm(FlaskForm):
    userid = StringField('UserID', validators=[DataRequired()])
    username = StringField('Username', validators=[
        DataRequired(),
        Regexp('^[A-Za-z]*$', message="Username should contain only letters")
    ])
    currentcompany = StringField('Current Company', validators=[
        DataRequired(),
        Regexp('^[A-Za-z0-9 ]*$', message="Current Company should not contain special characters")
    ])
    previouscompany = StringField('Previous Company', validators=[
        DataRequired(),
        Regexp('^[A-Za-z0-9 ]*$', message="Previous Company should not contain special characters")
    ])
    duration = StringField('Duration', validators=[DataRequired()])
    dateofbirth = StringField('Date of Birth', validators=[DataRequired()])
    submit = SubmitField('Submit')
