# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from database import obter_conexao
from modelos import User

app = Flask(__name__)
app.secret_key = 'chave-super-secreta'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        conn = obter_conexao()
        cursor = conn.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if user:
            flash('E-mail já cadastrado!', 'error')
            conn.close()
            return redirect(url_for('register'))

        hash_senha = generate_password_hash(senha)
        conn.execute("INSERT INTO users (email, senha) VALUES (?, ?)", (email, hash_senha))
        conn.commit()
        conn.close()

        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        conn = obter_conexao()
        cursor = conn.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user['senha'], senha):
            usuario = User(nome=email)
            usuario.id = user['id']
            login_user(usuario)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciais inválidas.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu com sucesso.', 'success')
    return redirect(url_for('index'))

# CRUD do próprio usuário

@app.route('/perfil')
@login_required
def perfil():
    conn = obter_conexao()
    usuario = conn.execute("SELECT * FROM users WHERE id = ?", (current_user.id,)).fetchone()
    conn.close()
    return render_template('perfil.html', usuario=usuario)

@app.route('/editar-perfil', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    conn = obter_conexao()

    if request.method == 'POST':
        novo_email = request.form['email']
        nova_senha = generate_password_hash(request.form['senha'])

        conn.execute("UPDATE users SET email = ?, senha = ? WHERE id = ?", (novo_email, nova_senha, current_user.id))
        conn.commit()
        conn.close()

        flash('Dados atualizados com sucesso!', 'success')
        return redirect(url_for('perfil'))

    usuario = conn.execute("SELECT * FROM users WHERE id = ?", (current_user.id,)).fetchone()
    conn.close()
    return render_template('editar_perfil.html', usuario=usuario)

@app.route('/excluir-conta', methods=['POST'])
@login_required
def excluir_conta():
    conn = obter_conexao()
    conn.execute("DELETE FROM users WHERE id = ?", (current_user.id,))
    conn.commit()
    conn.close()

    logout_user()
    flash('Sua conta foi excluída com sucesso.', 'success')
    return redirect(url_for('index'))
