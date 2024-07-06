from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def main():
    return render_template('index0.html')



@app.route('/curriculo')
def show_curriculo():
    return render_template('curriculo.html')


# Nova rota
@app.route('/pagina_inicial')
def paginaInicial():
    return render_template('pagina_inicial.html')




# if ... Sempre no final
if __name__=='__main__':
    app.run(debug=True)
