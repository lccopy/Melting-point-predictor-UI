from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_endpoint_status = "local" #local or online
app_status = "local" #local or online

def celsius_to_kelvin(celsius):
    return round((celsius + 273.15), 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        smiles = request.form.get('smiles')
        if api_endpoint_status == "local":
            api_url = "http://localhost:8000/predict"
            response = requests.get(api_url, params={'SMILES': smiles})
            melting_point = response.json()
            melting_point = melting_point.get('melting_point', 'unknown')


        if api_endpoint_status == "online":
            api_url = ""
            response = requests.get(api_url, params={'SMILES': smiles})
            melting_point = response.json()
            melting_point = melting_point.get('melting_point', 'unknown')

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
    if app_status == 'local':
        app.run(debug=False, port=5002)
    if app_status == 'online':
        app.run(debug=False)
