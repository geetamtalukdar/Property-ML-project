from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    bedrooms = float(request.form.get('bedrooms'))
    bathrooms = int(request.form.get('bathrooms'))
    price = int(request.form.get('price'))


    # prediction
    results = model.predict(np.array([bedrooms, bathrooms, price]).reshape(1,3))

    if results[0] == 1:
        result = 'waterfront'
    else:
        result = 'not waterfront'


    return render_template('index.html',result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)