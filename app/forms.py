from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
	login = TextField('m_login', validators = [Required()])
	password = TextField('m_password', validators = [Required()])
	remember_me = BooleanField('m_remember_me', default = False)



class RegisterForm(Form):
    login = TextField('m_login', validators = [Required()])
    password1 = TextField('m_password1', validators = [Required()])
    password2 = TextField('m_password2', validators = [Required()])