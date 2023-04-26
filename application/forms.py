from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Length


class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
    description = StringField('Description', validators=[DataRequired(), Length(min=2, max=200)])
    date_of_release = DateTimeField('Date Of Release', validators=[DataRequired()])
    submit = SubmitField('Create Movie')
