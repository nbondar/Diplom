from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
	login = TextField('m_login', validators = [Required()])
	password = TextField('m_password', validators = [Required()])
	remember_me = BooleanField('m_remember_me', default = False)