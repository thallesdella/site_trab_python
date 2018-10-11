from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Fazer Login')
	
class RegistrationForm(FlaskForm):
    username = StringField('Usuário:', validators=[DataRequired()])
    first_name = StringField('Primeiro Nome:', validators=[DataRequired()])
    last_name = StringField('Ultimo Nome:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField(
        'Confirme a Senha:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar-se')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Por favor, use um usuário diferente.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Por favor, use um email diferente.')
			
class EditForm(FlaskForm):
    first_name = StringField('Primeiro Nome:', validators=[DataRequired()])
    last_name = StringField('Ultimo Nome:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField(
        'Confirme a Senha:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Editar')
