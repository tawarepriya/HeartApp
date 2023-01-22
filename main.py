from flask import Flask, jsonify, render_template, request
from model.utils import HeartDisease
import config


app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome")
    return render_template("index.html")

@app.route('/predict_disease',methods=['GET','POST'])
def get_heart_disease():
    if request.method == "GET":
        print("We are using GET Method")

        data = request.form
        print("Data-->",data)

        age = eval(request.args.get('age'))
        sex = request.args.get('sex')
        cp = request.args.get('cp')
        trestbps = eval(request.args.get('trestbps'))
        chol = eval(request.args.get('chol'))
        fbs = request.args.get('fbs')
        restecg = request.args.get('restecg')
        thalach = eval(request.args.get('thalach'))
        exang = request.args.get('exang')
        oldpeak = eval(request.args.get('oldpeak'))
        slope = request.args.get('slope')
        ca = eval(request.args.get('ca'))
        thal = request.args.get('thal')


        print('age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal',age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)

        hd = HeartDisease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        disease = hd.get_predicted_disease()
        if disease == 1:
            return render_template("index.html",prediction="The patient has a heart disorder")
        else:
            return render_template("index.html",prediction="The patient has not heart disease.")

       
    else:
        print('we are using POST method')
       

        age = eval(request.form.get('age'))
        sex = request.form.get('sex')
        cp = request.form.get('cp')
        trestbps = eval(request.form.get('trestbps'))
        chol = eval(request.form.get('chol'))
        fbs = request.form.get('fbs')
        restecg = request.form.get('restecg')
        thalach = eval(request.form.get('thalach'))
        exang = request.form.get('exang')
        oldpeak = eval(request.form.get('oldpeak'))
        slope = request.form.get('slope')
        ca = eval(request.form.get('ca'))
        thal = request.form.get('thal')


        print('age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal',age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)

        hd = HeartDisease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        disease = hd.get_predicted_disease()
        # return render_template("index.html", prediction = disease)
        if disease == 1:
            return render_template("index.html",prediction="The patient has a heart disorder.")
        else:
            return render_template("index.html",prediction="The patient has not heart disease.")

    

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug = True)