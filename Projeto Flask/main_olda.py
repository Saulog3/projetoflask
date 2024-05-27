from flask import Flask, url_for, render_template

#inicialização
app = Flask(__name__)


# Rotas

@app.route("/")
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Saulo", "membro_ativo": True},
        {"nome": "Heitor", "membro_ativo": False},
        {"nome": "Helena", "membro_ativo": False},
    ]

    return render_template("index.html", titulo = titulo, usuarios = usuarios )


@app.route("/sobre")
def pagina_sobre():
    return """
        <b>ProgramadorPython</b>: assista os videos no
        <a href="https://youtube.com/@programadorpython">Canal no Youtube</a>
    """
#execução
app.run(debug=True)