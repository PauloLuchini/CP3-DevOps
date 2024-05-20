from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://myuser:mypassword@db/mydatabase?charset=utf8mb4&collation=utf8mb4_general_ci'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Empregado(db.Model):
    __tablename__ = 'empregado'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50, collation='utf8mb4_general_ci'))
    cargo = db.Column(db.String(50, collation='utf8mb4_general_ci'))

    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

@app.route('/empregados', methods=['GET'])
def get_empregados():
    empregados = Empregado.query.all()
    output = []
    for empregado in empregados:
        empregado_data = {'id': empregado.id, 'nome': empregado.nome, 'cargo': empregado.cargo}
        output.append(empregado_data)
    return jsonify({'empregados': output})

@app.route('/empregados', methods=['POST'])
def add_empregado():
    data = request.get_json()
    novo_empregado = Empregado(nome=data['nome'], cargo=data['cargo'])
    db.session.add(novo_empregado)
    db.session.commit()
    return jsonify({'message': 'Empregado criado com sucesso!'})

@app.route('/empregados/<int:empregado_id>', methods=['PUT'])
def update_empregado(empregado_id):
    empregado = Empregado.query.get(empregado_id)
    data = request.get_json()
    empregado.nome = data['nome']
    empregado.cargo = data['cargo']
    db.session.commit()
    return jsonify({'message': 'Empregado atualizado com sucesso!'})

@app.route('/empregados/<int:empregado_id>', methods=['DELETE'])
def delete_empregado(empregado_id):
    empregado = Empregado.query.get(empregado_id)
    db.session.delete(empregado)
    db.session.commit()
    return jsonify({'message': 'Empregado deletado com sucesso!'})
    
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
