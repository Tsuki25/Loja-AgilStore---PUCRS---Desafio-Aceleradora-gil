from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '56f9bc21b90ca30de475ee88ac2a4fc29985c5475467985b59361280a1e077bf0df560ca159a80bf90446a6fdb40d93c59030e82f1f7de15638e374d1e7ba3cc'  # Substitua por algo único e secreto

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.Text, nullable=False)
    qtde = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def listar_produtos():
    produtos = Produto.query.order_by(Produto.id).all()
    return render_template('lista_produtos.html', produtos=produtos)


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_produto():
    if request.method == 'POST':
        nome = request.form['nome_produto']

        produto_existente = Produto.query.filter_by(nome=nome).first()
        if produto_existente:
            flash("Já existe um produto com este nome.", "error")
            return render_template('cadastro_produtos.html')


        categoria = request.form['categoria']
        qtde = int(request.form['qtde'])
        valor = float(request.form['valor_produto'])

        novo_produto = Produto(nome=nome, categoria=categoria, qtde=qtde, valor=valor)
        db.session.add(novo_produto)
        db.session.commit()

        return redirect('/')  # Redireciona após salvar
    return render_template('cadastro_produtos.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    produto = Produto.query.get_or_404(id)

    if request.method == 'POST':
        produto.nome = request.form['nome_produto']

        produto_existente = Produto.query.filter_by(nome=produto.nome).first()
        if produto_existente:
            flash("Já existe um produto com este nome.", "error")
            return render_template('cadastro_produtos.html')

        produto.categoria = request.form['categoria']
        produto.qtde = int(request.form['qtde'])
        produto.valor = float(request.form['valor_produto'])
        db.session.commit()
        return redirect('/')

    return render_template('cadastro_produtos.html', produto=produto)

@app.route('/exclude/<int:id>', methods=['GET', 'POST'])
def excluir(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect('/')

@app.route('/buscar_produtos', methods=['GET'])
def buscar_produtos():
    # Pega o valor da query string
    busca = request.args.get('query', '').strip()

    if busca:
        produtos = Produto.query.filter(
            (Produto.nome.ilike(f'%{busca}%')) |
            (Produto.categoria.ilike(f'%{busca}%'))
        ).all()  # Retorna produtos que correspondem ao critério de busca
    else:
        produtos = Produto.query.all()  # Se não houver busca, exibe todos os produtos

    return render_template('lista_produtos.html', produtos=produtos)