from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load saved model pipeline (preprocessing + model)
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            # Read inputs as raw strings / numbers — NO manual encoding
            age = int(request.form['age'])
            sex = request.form['sex']          # 'male' or 'female'
            bmi = float(request.form['bmi'])
            children = int(request.form['children'])
            smoker = request.form['smoker']    # 'yes' or 'no'
            region = request.form['region']    # 'southwest', 'southeast', 'northwest', 'northeast'

            # Create DataFrame exactly as training features (categorical as strings)
            input_df = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
                                    columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

            # Predict with pipeline — automatic preprocessing
            pred = model.predict(input_df)[0]
            prediction = f"₹ {pred:,.2f}"

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
