from flask import *
import json

produtos = []

app = Flask(__name__)
    
auxiliar = 0

@app.route('/produto', methods=['GET'])
def index():         
    return jsonify({'Produtos': produtos})

@app.route('/produto/<int:idProduto>', methods=['GET'])
def getProduto(idProduto):
    produto = [produto for produto in produtos if produto['id'] == idProduto]

    if(len(produto) == 0):
        return jsonify({'Error': 'Produto não encontrado'}), 404

    return jsonify({'Produto': produto})


@app.route('/produto', methods=['POST'])
def addProduto():
    if not request.json:
        abort(400)

    
    global auxiliar
    auxiliar = auxiliar + 1

    produto = {
        'id': auxiliar,        
        'name': request.json['name'],
        'preco': request.json['preco'],
        'quantidade': request.json['quantidade']
    }
    
    produtos.append(produto)
    return jsonify({'produto': produto})



@app.route('/produto/<int:idProduto>', methods=['DELETE'])
def deleteProduto(idProduto):
    produto = [produto for produto in produtos if produto['id'] == idProduto]

    if(len(produto) == 0):
        return jsonify({'Error': 'Produto não encontrado'}), 404

    
    produtos.remove(produto[0])

    return jsonify({'produto': produto}), 200

@app.route('/produto/<int:idProduto>', methods=['PUT'])
def updateProduto(idProduto):
    produto = [produto for produto in produtos if produto['id'] == idProduto]

    if(len(produto) == 0):
        return jsonify({'Error': 'Produto não encontrado'}), 404

    if 'name' in request.json:
        produto[0]['name'] = request.json['name']
    if 'preco' in request.json:
        produto[0]['preco'] = request.json['preco']
    if 'quantidade'  in request.json:
        produto[0]['quantidade'] = request.json['quantidade']

    return jsonify({'Produto': produto})

app.run()