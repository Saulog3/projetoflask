from flask import Blueprint, render_template
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)


'''
Rota de Clientes

    - /clientes/ (GET) - Listar os clientes
    - /clientes/ (POST) - Inserir um cliente no servidor
    - /clientes/new (GET) - Renderizar o formulario para criar um cliente
    - /clientes/<id> (GET) - obter os dados de um cliente
    - /clientes/<id>/edit (GET) - Renderizar um formulario para editar um cliente
    - /clientes/<id>/update (PUT) - Atualizar os dados do cliente
    - /clientes/<id>/delete (DELETE) - deleta o registro do usuario 
'''



@cliente_route.route('/')
def lista_cliente():
    """ Listar os Clientes """

    return render_template('lista_clientes.html', clientes=CLIENTES)



@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Inserir dados do cliente """
    pass



@cliente_route.route('/new', methods=['GET'])
def form_cliente():
    """Formulário para cadastrar um cliente """  
    return render_template('form_cliente.html')



@cliente_route.route('/<int:cliente_id>')
def detelhe_cliente(cliente_id):
    """ Exibir detelhes de um cliente """  
    return render_template('detalhe_cliente.html')


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ Formulário para editar um cliente """  
    return render_template('form_edit_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ Atualizar informações do cliente """  
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['PUT'])
def deletar_cliente(cliente_id):
    """ Atualizar informações do cliente """  
    pass




