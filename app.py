from flask import Flask, render_template

app = Flask(__name__)

# Ruta de la página de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Ruta de la página de servicios
@app.route('/servicios')
def servicios():
    return render_template('servicios.html')


if __name__ == '__main__':
    app.run(debug=True)