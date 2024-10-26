from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    firstname = StringField('Imię')
    lastname = StringField('Nazwisko')
    email = StringField('E-mail', validators=[DataRequired('Musisz podać e-mail'), Email('Podaj prawidłowy adres e-mail')])
    company = StringField('Firma')
    details = TextAreaField('Szczegóły', validators=[DataRequired('Musisz podać szczegóły')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Wyślij')
    
    