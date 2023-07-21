from flask import Flask, render_template,request
from gerar_senha import gerar



app = Flask(__name__)

@app.route('/')
def homepage():

    return render_template('home.html')

@app.route('/gerar_senha', methods=['GET','POST'])
def gerar_senha():
    
    select_maiu = request.args.get('maiu')
    select_min = request.args.get('min')
    select_num = request.args.get('num')
    select_simb = request.args.get('simb')
    tamanho = request.args.get('vol')
    print(tamanho)
    
    senha =  gerar(select_maiu,select_min, select_num,select_simb,tamanho)
    texto_senha = senha

    return render_template('home.html',texto_senha=texto_senha)






if __name__ == '__main__':
    app.run(debug=True)