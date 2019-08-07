from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route("/")
def welcome():
    # return "Welcome to Flask"
    return render_template('index.html')

# def linear_model(x):
#     model=joblib.load("gdp_model.sav")
#     ls_value = model.predict([[x]])
#     return ls_value[0]

@app.route("/LinearRegression", methods=['POST', 'GET'])
def linear():
    # linear_model(42000)
    # return "Learning linear regression"
    # return render_template("linear_regression.html")

    if request.method == "POST":
        data = request.form
        country_name = data["name"]
        gdp = data["gdp"]
        gdp = int(gdp)
        ls_value = linear_model(gdp)
        return str(ls_value)

if __name__ == '__main__':
    app.run()