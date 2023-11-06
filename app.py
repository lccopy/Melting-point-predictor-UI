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

if __name__ == '__main__':
    app.run(debug=False)
