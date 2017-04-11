from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
	email = TextField('email', validators = [Required()])
	password = TextField('password', validators = [Required()])
	remember_me = BooleanField('remember_me', default = False)



class RegisterForm(Form):
    email = TextField('email', validators = [Required()])
    nickname = TextField('nickname', validators = [Required()])
   # password1 = TextField('password1', validators = [Required()])
   # password2 = TextField('password2', validators = [Required()])


class ProfileForm(Form):
    #login = TextField('m_login', validators = [Required()])
    nickname = TextField('nickname', validators = [Required()])
    #password1 = TextField('m_password1', validators = [Required()])
    ##password2 = TextField('m_password2', validators = [Required()])
    surname = TextField('surname')
    name = TextField('name')
    phonenumber = TextField('phonenumber')
    balance = TextField('balance')
  

class NamespaceForm(Form):
	namespace = TextField('namespace', validators = [Required()])    