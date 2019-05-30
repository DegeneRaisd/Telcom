from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = 'telcom'

class Cliente:
    def __init__(self, id, nome, telefone):
        self.id = id
        self.nome = nome
        self.telefone = telefone

class Funcionario:
    def __init__(self, id, nome, telefone, departamento):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.departamento = departamento

class Usuario:
    def __init__(self, id, senha):
        self.id = id
        self.senha = senha

F1 = Funcionario('00001', 'Marcão', '4002-8922', 'ADM')
F2 = Funcionario('00002', 'Marcião', '4002-8922', 'T.I')
listaF = [F1, F2]

C1 = Cliente('001', 'Marcio', '4002-8922')
C2 = Cliente('002', 'Mario', '4002-8922')
listaC = [C1, C2]

usuario1 = Usuario('001', '1234')
usuario2 = Usuario('002', '1234')
usuario3 = Usuario('003', '1234')

usuarios = {usuario1.id: usuario1,
            usuario2.id: usuario2,
            usuario3.id: usuario3}


@app.route('/')
def logar():
    return render_template('home.html')

@app.route('/select')
def select():
    return render_template('selectTable.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html', titulo='Tabela Clientes', names=listaC)

@app.route('/funcionarios')
def funcionarios():
    return render_template('funcionarios.html', titulo='Tabela Funcionarios', func=listaF)

@app.route('/novof')
def novof():
    return render_template('nfunc.html', titulo='Novo Funcionario')

@app.route('/novoc')
def novoc():
    return render_template('nclie.html', titulo='Novo Cliente')

@app.route('/criarf', methods=['POST',])
def createf():
    id = request.form['id']
    nome = request.form['nome']
    telefone = request.form['telefone']
    departamento = request.form['departamento']
    nfunc = Funcionario(id, nome, telefone, departamento)
    listaF.append(nfunc)
    return render_template('funcionarios.html', titulo='Lista de Funconarios', func=listaF)

@app.route('/criarc', methods=['POST',])
def createc():
    id = request.form['id']
    nome = request.form['nome']
    telefone = request.form['telefone']
    nclie = Cliente(id, nome, telefone)
    listaC.append(nclie)
    return render_template('clientes.html', titulo='Lista de Clientes', names=listaC)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['user'] in usuarios:
        usuario = usuarios[request.form['user']]
        if usuario.senha == request.form['pass']:
            session['usuario_logado'] = usuario.id
            flash(usuario.id + ' logou com sucesso!')
        return redirect('/select')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/')

app.run()