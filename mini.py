from flask import Flask, render_template, request
import pickle
import numpy as np

import warnings
import sys

if not sys.warnoptions:
    warnings.simplefilter("ignore")
warnings.filterwarnings("ignore", category=DeprecationWarning)

model = pickle.load(open('mini.pkl', 'rb'))

app = Flask(__name__, template_folder='templates')


@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    name = request.form['NAME']
    address = request.form['ADDRESS']
    email = request.form['EMAIL']
    app_income1 = request.form['APP_INCOME']
    coapp_income1 = request.form['COAPP_INCOME']
    loan_amount1 = request.form['LOAN_AMOUNT']
    la_term1 = request.form['LA_TERM']
    cr_history1 = request.form['CR_HISTORY']
    married1 = request.form['MARRIED']
    gender1 = request.form['GENDER']
    dependents1 = request.form['DEPENDENTS']
    education1 = request.form['EDUCATION']
    self_emp1 = request.form['SELF_EMP']
    mobile1 = request.form['MOBILE']
    property1 = request.form['PROPERTY']
    app_income = int(app_income1)
    coapp_income = int(coapp_income1)
    loan_amount = int(loan_amount1)
    la_term = int(la_term1)
    if (cr_history1 == 'Clear'):
        cr_history = 1.0
    else:
        cr_history = 0.0
    if (married1 == 'YES'):
        married = 1
    else:
        married = 0
    if (gender1 == 'MALE'):
        gender = 1
    else:
        gender = 0
    dependents_0 = 0
    dependents_1 = 0
    dependents_2 = 0
    dependents_3 = 0
    if (dependents1 == 'zero'):
        dependents_0 = 1
    if (dependents1 == 'one'):
        dependents_1 = 1
    if (dependents1 == 'two'):
        dependents_2 = 1
    if (dependents1 == 'three_plus'):
        dependents_3 = 1
    if (education1 == 'Graduate'):
        education = 1
    else:
        education = 0
    if (self_emp1 == 'yes'):
        self_emp = 1
    else:
        self_emp = 0
    mobile = int(mobile1)
    p_rural = 0
    p_semi_urban = 0
    p_urban = 0
    if (property1 == "rural"):
        p_rural = 1
    if (property1 == "semi-urban"):
        p_semi_urban = 1
    if (property1 == "urban"):
        p_urban = 1
    # arr=np.array([3366	,2200.0	,135.0	,360.0	,1.0	,1	,1	,1	,0	,0	,0	,1	,0	,1	,0	,0])
    arr = np.array(
        [app_income, coapp_income, loan_amount, la_term, cr_history, gender, married, dependents_0, dependents_1,
         dependents_2, dependents_3, education, self_emp, p_rural, p_semi_urban, p_urban])
    pred = model.predict(arr.reshape(1, -1))
    return render_template('prediction_page.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)