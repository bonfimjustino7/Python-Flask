from flask import Flask, render_template, request, url_for, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'

db = SQLAlchemy(app)

class Pessoa(db.Model):
	
	__tablename__ = 'cliente'

	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String)
	telefone = db.Column(db.String)
	cpf = db.Column(db.String)
	email = db.Column(db.String)


	def __init__(self, nome, telefone, cpf, email):
		self.nome = nome
		self.telefone = telefone
		self.cpf = cpf
		self.email = email

db.create_all()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/clientes')
def clientes():
	return render_template('clientes.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
	if request.method == 'POST':
		nome = request.form.get('nome')
		telefone = request.form.get('telefone')
		cpf = request.form.get('cpf')
		email = request.form.get('email')

		if nome and telefone and cpf and email:
			p = Pessoa(nome, telefone, cpf, email)
			db.session.add(p)
			db.session.commit()

	return redirect(url_for('index'))

@app.route('/lista')
def lista():
	pessoas = Pessoa.query.all()
	return render_template('lista.html', pessoas=pessoas)

if __name__ == '__main__':
	app.run(debug=True)

