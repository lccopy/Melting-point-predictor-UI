from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def celsius_to_kelvin(celsius):
    return celsius + 273.15

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        smiles = request.form.get('smiles')
        #api call and preprocessing
        melting_point = 42  # dummie value
        k_melting_point = celsius_to_kelvin(melting_point)

        return render_template('result.html', smiles=smiles, melting_point=melting_point, k_melting_point=k_melting_point)

    return render_template('index.html')

@app.route('/method')
def method():
    return render_template("method.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")


@app.route('/contribute')
def contribute():
    return render_template("contribute.html")

if __name__ == '__main__':
    app.run(debug=False)
