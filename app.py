from flask import Flask
from flask import render_template
from powerapp.marvel import liste_personnage
# Pensez à faire pip install flask

app = Flask(__name__)

@app.route('/')
def main():
    liste = liste_personnage()
    return render_template('index.html', perso=liste)

@app.route('/coucou/')
def deux():
    return "<h1> Super site</h1>"

if __name__ == '__main__':
    app.run(debug=True)
