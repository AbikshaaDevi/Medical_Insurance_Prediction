from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        age = int(request.form.get('age', 0))
        sex = request.form.get('sex', 'male')
        bmi = float(request.form.get('bmi', 0.0))
        children = int(request.form.get('children', 0))
        smoker = request.form.get('smoker', 'no')
        region = request.form.get('region', 'southwest')

        input_df = pd.DataFrame([{
            'age': age,
            'sex': sex,
            'bmi': bmi,
            'children': children,
            'smoker': smoker,
            'region': region
        }])

        pred = model.predict(input_df)[0]
        prediction = f"{pred:,.2f}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)