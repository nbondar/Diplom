from flask import *
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, login_manager
from forms import LoginForm, RegisterForm, ProfileForm, NamespaceForm
from models import User, Namespace
from datetime import *


@app.route('/')
@app.route('/index')
def main():
    user = { 'login': '' }
    return render_template("main.html",
        title = 'Bullshit')


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("dashboard.html",
        title = 'Dashboard',
        current_user=current_user)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def Profile():
  form = ProfileForm()
  form.name.data = current_user.name
  form.surname.data = current_user.surname
  form.phonenumber.data = current_user.phonenumber
  form.nickname.data = current_user.nickname
  form.balance.data = current_user.balance
  return render_template("profile.html",
    title = 'Profile',
    current_user=current_user,
    form = form)


@app.route('/login', methods = ['GET', 'POST']) 
def login():
  # if g.user is not None and g.user.is_authenticated():
  #     return redirect(url_for('/'))
  #form = LoginForm(request.form)
  #if form.validate_on_submit():
  #     session['remember_me'] = form.remember_me.data  
  #     return redirect(url_for('dashboard'))
  return render_template('login.html',
    title = 'Sign In !',
    # form = form,
    providers = app.config['LOGIN_PASS'])


@app.route('/Registration', methods=['GET','POST']) 
def register():
 #form = RegisterForm()   
 return render_template('register.html',
    title = 'Register!)')
    #form = form)


@app.route('/add', methods=['GET', 'POST'])
def add_new_user():
    json_from_client = request.json
    email = json_from_client["email"]
    nickname = json_from_client["nickname"]
    password = json_from_client["password"]
    users = User.query.filter_by(email=email).first()
    if users:
        result = {"status": "this user already exists"}
        return jsonify(result=result)
    else:
        new_user = User(email = email, nickname = nickname, passw = password)
        db.session.add(new_user)
        db.session.commit()
        result = {"status": "OK"}
        return jsonify(result=result) 


@app.route('/ok', methods=['GET', 'POST'])
def ok():
  return render_template('ok.html')



@app.route('/enter', methods=['GET', 'POST'])
def enter():
    json_from_client = request.json
    email = json_from_client["email"]
    password = json_from_client["password"]
    user = User.query.filter_by(email=email).first()
    if user.passw == password:  
            result = {"status": "OK"}
            login_user(user)
            return jsonify(result=result)
    else:
        result = {"status": "login/password wrong or not exist"}
        return jsonify(result=result)      




@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')    



@app.route('/changepassword', methods=['GET', 'POST'])
@login_required
def changepassword(): 
   return render_template("changepassword.html",
    title = 'ChangePassword',
    current_user=current_user)


@app.route('/saveprofile', methods=['GET', 'POST'])
@login_required
def saveprofile():
    json_from_client = request.json
    email = json_from_client["email"]
    current_user = User.query.filter_by(email=email).first()
    current_user.name = json_from_client["name"]
    current_user.nickname = json_from_client["nickname"]
    current_user.surname = json_from_client["surname"]
    current_user.phonenumber = json_from_client["phonenumber"]
    #db.session.update(current_user)
    db.session.commit()
    result = {"status": "OK"}
    return jsonify(result=result) 




@app.route('/newnamespace', methods=['GET','POST'])
@login_required
def newnamespace():
  form = NamespaceForm()
  id = current_user.id
  namespaces = Namespace.query.filter_by(user_id=id).all()
  count = len(namespaces)
  return render_template("newnamespace.html",
    title = 'Create namespace',
    current_user=current_user,
    namespaces = namespaces,
    form = form,
    count = count)


@app.route('/namespace', methods=['GET','POST'])
@login_required
def namespace():
    json_from_client = request.json
    name = json_from_client["name"]
    id = json_from_client["id_u"]
    timestamp = datetime.now()
    current_namespace = Namespace.query.filter_by(name=name, user_id=id).first()
    if current_namespace:
        result = {"status": "already exist"}
        return jsonify(result=result)
    else:
        new_namespace = Namespace(user_id = id, name = name, timestamp=timestamp,count=0)
        db.session.add(new_namespace)
        db.session.commit()
        result = {"status": "OK" , "timestamp":timestamp}
        return jsonify(result=result) 



@app.route('/password', methods=['GET','POST'])
@login_required
def password():
    