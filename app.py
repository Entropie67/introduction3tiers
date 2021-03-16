from flask import Flask
from flask import render_template

# Pensez à faire pip install flask

app = Flask(__name__)

@app.route('/')
def main():
    prenom = "Olivier"
    return render_template('index.html', nom=prenom)

@app.route('/coucou/')
def deux():
    return "<h1> Super site</h1>"

if __name__ == '__main__':
    app.run(debug=True)
