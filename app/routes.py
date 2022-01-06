from app import app, db
from flask import render_template,url_for,redirect,request,flash
from app.models import Asset, User
from app.forms import AddAssetForm, LoginForm
from flask_login import current_user, login_user

@app.route('/')
@app.route('/index')
def index():
    # Renderowanie głównej strony index.html z folderu templates
    text = "This is infraapp"
    return render_template('index.html', title='Infrapp', text=text)

@app.route('/assets')
def assets():
    # Pobranie assetów z bazy danych
    # Przypisanie ich do zmiennej assets
    # Przekazanie assetów do metody render_template
    assets = Asset.query.all()
    return render_template('assets.html', title='Assets', assets=assets)

@app.route('/add_asset', methods=['GET', 'POST'])
def add_asset():
    """
    Przypisanie formularza AddAssetForm do zmiennej form
    Jeśli formularz jest poprawny i wypełniony :
     - Utworzenie assetu, pobierając dane z formularza;
     - Dodanie assetu do bazy danych oraz potwierdzenie - add, commit ;
     - Powrót do strony z assetami;
    """ 
    form = AddAssetForm()
    if form.validate_on_submit():
        asset = Asset(name=form.name.data, type=form.type.data, purchased=form.purchased.data, owner = form.owner.data, serial_number = form.serial_number.data)
        db.session.add(asset)
        db.session.commit()
        return redirect(url_for('assets'))
    return render_template('add_asset.html',title = 'Add asset', form=form)

@app.route('/asset/<int:asset_id>')
def asset(asset_id):
    # Wyszukanie konkretnego assetu oraz wyrenderowanie go na stronie asset.html
    asset = Asset.query.filter_by(id=asset_id).first_or_404()
    return render_template('asset.html',asset=asset)

@app.route('/delete/<int:asset_id>')
def delete(asset_id):
    """
    Usuwanie assetu z bazy danych :
        1. Znajdź asset i przypisz go do zmiennej;
        2. Usuń asset - delete; potwierdź zmiany - commit;
        3. Powrót do strony z assetami;
    """
    asset = Asset.query.filter_by(id=asset_id).first_or_404()
    db.session.delete(asset)
    db.session.commit()
    return redirect(url_for('assets'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)