from flask import Flask, Blueprint, request, jsonify, render_template
import sqlite3

cliente = Blueprint('cliente', __name__)

def conectar():
    return sqlite3.connect('database/data.db')

@cliente.route('/cliente', methods=['GET'])
def get_all():
    clientes = []
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_cliente")

        for i in cur.fetchall():
            cliente = {}
            cliente["cpf"] = i["cpf"]
            cliente["nome"] = i["nome"]
            cliente["email"] = i["email"]
            cliente["telefone"] = i["telefone"]
            clientes.append(cliente)
    except Exception as e:
        print(e)
        clientes = []

    return jsonify(clientes)

@cliente.route('/cadastro', methods=['POST'])
def insert():
    cliente = request.get_json()

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("INSERT INTO tb_cliente (cpf, nome, email, telefone) VALUES (?, ?, ?, ?)", (cliente['cpf'], cliente['nome'], cliente['email'], cliente['telefone']))
        conn.commit()
        resposta = jsonify({'mensagem':'Operacao realizada com sucesso'})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return resposta

@cliente.route('cliente/<cpf>', methods=['GET'])
def get_by_cpf(cpf):
    cliente = {}
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_cliente where cpf=?",(cpf))
        row = cur.fetchone()
       
        cliente["cpf"] = row["cpf"]
        cliente["nome"] = row["nome"]
        cliente["email"] = row["email"]
        cliente["telefone"] = row["telefone"]
           
    except Exception as e:
        print(str(e))
        cliente = {}

    return jsonify(cliente)

@cliente.route('/edit_clente/<cpf>',  methods = ['PUT'])
def update():
    cliente = request.get_json()

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE tb_cliente SET nome=?, email=?, telefone=? WHERE cpf=?",
                    (cliente['nome'], cliente['email'], cliente['telefone'], cliente['cpf']) )
        conn.commit()
        resposta = jsonify({'mensagem':'Operacao realizada com sucesso'})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return resposta

@cliente.route('/del_cliente/<cpf>',  methods = ['DELETE'])
def delete(cpf):
    print(cpf)
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM tb_cliente WHERE cpf=?",(cpf,))
        conn.commit()
        resposta = jsonify({'mensagem':'Registro apagado com sucesso'})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return resposta

@cliente.route('/produto', methods=['GET'])
def get_all_prod():
    clientes = []
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_produtos")

        for i in cur.fetchall():
            cliente = {}
            cliente["codigo"] = i["codigo"]
            cliente["nome"] = i["nome"]
            clientes.append(cliente)
    except Exception as e:
        print(e)
        clientes = []

    return jsonify(clientes)

@cliente.route('/cadastro_produto', methods=['POST'])
def insert_prod():
    cliente = request.get_json()

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("INSERT INTO tb_produtos (codigo, nome) VALUES (?, ?)", (cliente['codigo'], cliente['nome']))
        conn.commit()
        resposta = jsonify({'mensagem':'Operacao realizada com sucesso'})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return resposta

@cliente.route('produto/<codigo>', methods=['GET'])
def get_by_code_prod(codigo):
    cliente = {}
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_produtos where codigo=?",(codigo))
        row = cur.fetchone()
       
        cliente["codigo"] = row["codigo"]
        cliente["nome"] = row["nome"]
           
    except Exception as e:
        print(str(e))
        cliente = {}

    return jsonify(cliente)

@cliente.route('/edit_produto/<codigo>',  methods = ['PUT'])
def update_prod():
    cliente = request.get_json()

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE tb_produtos SET nome=? WHERE codigo=?",
                    (cliente['nome'], cliente['codigo']) )
        conn.commit()
        resposta = jsonify({'mensagem':'Operacao realizada com sucesso'})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return resposta

@cliente.route('/del_produto/<codigo>',  methods = ['DELETE'])
def delete_prod(codigo):
    print(codigo)
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM tb_produtos WHERE codigo=?",(codigo))
        conn.commit()
        resposta = jsonify({'mensagem':'Registro apagado com sucesso'})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return resposta