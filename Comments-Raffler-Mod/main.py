from flask import Flask, render_template, request
from sorteador import sorteador

# The flask is used to receive information from the HTML page, this is where you must run the program for it to work!
# O flask é utilizado para receber as informações da página HTML, rotas são criadas e redirecionam para algum lugar.
# É aqui que você deve executar o programa para que ele funcione!

app = Flask("Sorteio")
@app.route('/')
def index():
  return render_template('index.html')

# indica a rota para o HTML result
# go to result.html
@app.route('/result')
def result():
  try:
    url = request.args.get('url')
    number = int(request.args.get('winners'))
    remove_repeated = request.args.get('remove_repeated')
    resultado = sorteador(url, number, remove_repeated)
    return render_template('result.html', result = resultado[1], number = number, comments = resultado[0])
    
  except:
    print('Ocorreu um erro, tente novamente!')
    #return redirect('/')
    #redireciona para a página inicial
    return render_template('index.html')

  
app.run(host='0.0.0.0')

