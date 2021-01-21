import flask
from flask import request
from main import deletar_arquivos




render_template = flask.render_template  # Pointing to local module.
Flask = flask.Flask  # Pointing to local module.
app = Flask(__name__)


@app.route('/main_page')
def home():

    # print('chegou aqui')

    return render_template('home.html')



@app.route('/another_page', methods=['POST'])
def new_home():

    cep = request.form.get('cep')
    results = deletar_arquivos(cep)
    # print('CEP é:', cep)
    # print('chegou another page')


    return render_template('home2.html', results=results)


if __name__== '__main__':
    app.run(debug=True, port=6035)




