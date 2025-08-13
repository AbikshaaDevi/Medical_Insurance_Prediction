from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the saved pipeline (preprocessing + model)
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            # Read raw inputs (categoricals as strings, numerics as numbers)
            age = int(request.form['age'])
            sex = request.form['sex']          # 'male' / 'female'
            bmi = float(request.form['bmi'])
            children = int(request.form['children'])
            smoker = request.form['smoker']    # 'yes' / 'no'
            region = request.form['region']    # 'southwest' / 'southeast' / 'northwest' / 'northeast'

            # Pack into a DataFrame with the exact training columns
            input_df = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
                                    columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

            # Predict
            pred = model.predict(input_df)[0]
            prediction = f"₹ {pred:,.2f}"  # format with rupee symbol
        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
