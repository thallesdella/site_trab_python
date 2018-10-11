from flask import render_template, flash, redirect, request, url_for, session
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditForm
from app.models import User
from werkzeug.urls import url_parse
from datetime import datetime

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Usuário ou Senha inválidos')
            return redirect(url_for('index'))
        login_user(user, remember=form.remember_me.data)
        session['user_login'] = user.id
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('dashboard')
        return redirect(next_page)
    return render_template('login.html', title='Login', app=app, form=form)

@app.route('/registrar', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, email=form.email.data, first_name=form.first_name.data, last_name=form.last_name.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Parabens, você completou seu registro!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', app=app, form=form)
	
@app.route('/conta/<username>/<action>')
@login_required
def user(username, action):
    user = User.query.filter_by(username=username).first_or_404()
    form = EditForm()
    edit = True if action == 'editar' else False
    if form.validate_on_submit():
        current_user.email=form.email.data
        current_user.first_name=form.first_name.data
        current_user.last_name=form.last_name.data
        
        user.set_password(form.password.data)
        db.session.commit()
        flash('Parabens, alterou com sucesso o registro!')
        return redirect(url_for('user', username=current_user.username))
    elif request.method == 'GET':
        form.email.data=current_user.email
        form.first_name.data=current_user.first_name
        form.last_name.data=current_user.last_name
    return render_template('user.html', app=app, user=user, form=form, edit=edit)

@app.route('/logoff')
@login_required
def logout():
    session.pop('user_login', None)
    logout_user()
    return redirect(url_for('login'))

@app.route('/new-pass')
def rpass():
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def dashboard():
    user = User.query.filter_by(id=session['user_login']).first_or_404()
    return render_template('dashboard.html', app=app, user=user)
    
@app.route('/dontpad/<action>')
@login_required
def dontpad(action):
    user = User.query.filter_by(id=session['user_login']).first_or_404()
    return render_template('dontpad.html', app=app, user=user)
