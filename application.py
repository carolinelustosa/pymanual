from flask import Flask, render_template #importando o flask (#pip3 install flask)


application = Flask(__name__) #instanciando a app dentro do flask


@application.route('/') #endpoint
def main():
    return render_template('index.html')
