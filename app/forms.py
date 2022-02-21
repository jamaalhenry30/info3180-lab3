import os
from flask_wtf import Flaskform
from wtforms import StringField, TextField
from wtforms.validators import DataRequired,Email


class ContactForm(Flaskform):
    name = StringField('Name', validators=[DataRequired()])
    email= StringField('E-mail', validators=[DataRequired(),Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextField('Message', validators=[DataRequired()])