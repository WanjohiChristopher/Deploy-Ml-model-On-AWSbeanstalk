from flask import Flask, render_template, request
import pickle
import numpy as np

application = Flask(__name__)
model = pickle.load(open('diabetes.pkl', 'rb'))


@application.route('/')
def home():
    return """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="../templates/index.css" />

    <title>Diabetes Prediction</title>
</head>
<style>
    * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    }
    
    body {
        background-color: rgb(161, 161, 170);
        color: #407bff;
    }
    
    .container {
        margin-top: 30px;
        margin-left: 100px;
        margin-right: 100px;
    }
    
    h2 {
        font-size: 3rem;
        margin-bottom: 30px;
        margin-left: 30px;
        font-weight: 900px;
        color: rgb(63, 60, 60);
    }
    
    h3 {
        color: red;
        padding-left: 40px;
    }
    
    .row {
        display: flex;
    }
    
    .row .col-sm-6 {
        max-width: 50%;
        flex-basis: 50%;
    }
    
    .row .col-sm-6 img {
        object-fit: cover;
        margin-left: -10px;
    }
    
    .row .col-sm-6 {
        margin-left: 20px;
    }
    
    .row .col-sm-6 input {
        width: 80%;
        height: 60px;
        padding-left: 20px;
        border: none;
        border-bottom: 2px solid red;
        margin-top: 20px;
        font-size: 25px;
        color: red;
        border-radius: 5px;
        background-color: rgb(149, 149, 153);
    }
    
    .row .col-sm-6 input:focus {
        outline: none;
    }
    
    .row .col-sm-6 input::placeholder {
        color: #ffff;
    }
    
    .submit {
        width: 200px;
        height: 60px;
        color: #ffff;
        background-color: green;
        border-radius: 20px;
        margin-top: 20px;
        font-size: 20px;
    }
    
    .submit:focus {
        outline: none;
    }
    
    footer {
        background-color: #000;
    }
    
    footer p {
        text-align: center;
        font-size: 20px;
        padding-bottom: 20px;
        color: #ffff;
        padding-top: 20px;
    }
    
    @media only screen and (max-width: 660px) {
        .row {
            display: block;
        }
        .row .col-sm-6 {
            max-width: 100%;
            flex-basis: 100%;
        }
        .row .col-sm-6 input {
            width: 100%;
        }
    }
    
    @media only screen and (max-width: 372px) {
        .container {
            margin-top: 30px;
            margin-left: 50px;
            margin-right: 50px;
        }
        .row {
            display: block;
        }
        .row .col-sm-6 {
            max-width: 100%;
            margin: 0px;
            flex-basis: 1;
        }
        .pred {
            color: black;
            max-width: 200px;
            display: block;
            padding-top: 10px;
        }
        h2 {
            font-size: 35px;
            width: 100%;
        }
        .row .col-sm-6 img {
            width: 300px;
            margin-left: -20px;
        }
    }
    
    @media only screen and (max-width: 400px) {
        .container {
            margin-top: 30px;
            margin-left: 50px;
            margin-right: 50px;
        }
        .row {
            display: block;
        }
        .row .col-sm-6 {
            max-width: 100%;
            margin: 0px;
            flex-basis: 1;
        }
        h2 {
            font-size: 35px;
            width: 100%;
        }
        .row .col-sm-6 img {
            width: 300px;
            margin-left: -20px;
        }
    }
    
    @media only screen and (max-width: 500px) {
        .container {
            margin-top: 30px;
            margin-left: 50px;
            margin-right: 50px;
        }
        .row {
            display: block;
        }
        .row .col-sm-6 {
            max-width: 100%;
            margin: 0px;
            flex-basis: 1;
        }
        h2 {
            font-size: 35px;
            width: 100%;
        }
        .row .col-sm-6 img {
            width: 300px;
            margin-left: -20px;
        }
    }
    
    @media only screen and (max-width: 800px) {
        .container {
            margin-top: 30px;
            margin-left: 50px;
            margin-right: 50px;
        }
    }
</style>

<body>
    <section>
        <div class="container">
            <h2>Diabetes Prediction</h2>

            <div class="row">
                <div class="col-sm-6">
                    <div class="text">
                        <img src="Diabetes-rafiki.svg" alt="" srcset="" />
                    </div>
                </div>
                <div class="col-sm-6">
                    <h3>Dear Patient Kindly Fill the Your Health Status Below*</h3>

                    <form action="{{ url_for('predict')}}" method="post">
                        <input type="number" min="0" required name="Glucose" placeholder="Glucose " id="" />
                        <input type="number" min="0" required name="Pregnancies" placeholder="Pregnancies" id="" />
                        <input type="number" min="0" required name="BloodPressure" placeholder="Blood Pressure " id="" />
                        <input type="number" min="0" required name="SkinThickness" placeholder="Skin Thickness " id="" />
                        <input type="number" min="0" required name="Insulin" placeholder="Insulin Levels " id="" />
                        <input type="text" max="1" required name="DiabetesPedigreeFunction" placeholder="Diabetes Pedigree Function" id="" />
                        <input type="text" min="0" required name="BMI" placeholder="BMI " id="" />
                        <input type="number" min="0" required name="Age" placeholder="Age " id="" />
                        <button type="submit" min="0" required class="submit">
                Predict
              </button>
                    </form>
                    <br />
                    <b> <span style="color: black"> {{pred}} </span></b>
                </div>
            </div>
        </div>
    </section>
    <footer>
        <hr />
        <p>&copysr;Cursorhub Technologies Ltd &copy; 2021 All Right Reserved</p>
    </footer>
</body>

</html>"""


@application.route('/predict', methods=['POST'])
def predict():
    print(request.form)
    # taking data from the form
    features = [float(x) for x in request.form.values()]
    # keeping the features in an array
    feature_arr = [np.array(features)]
    # print(feature_arr)
    # performing prediction on our model
    prediction = model.predict(feature_arr)
    outcome = round(prediction[0], 2)

    if outcome == 1:
        return render_template('deploy.html', pred=' Dear Patient according to the Details you provided :You  have Diabetes.Please seek medical assistance🙏\n{}'.format(outcome))
    else:
        return render_template('deploy.html', pred='Dear Patient according to the Details you provided : You   Dont have Diabetes.Continue keeping safe🤗\n{}'.format(outcome))


if __name__ == '__main__':
    application.run(debug=True)