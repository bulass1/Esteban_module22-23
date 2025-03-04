from flask import Flask, render_template, request

app = Flask(__name__)

def check_diabetes(blood_sugar):
    if blood_sugar >= 126:
        return "Diabetic"
    else:
        return "Not Diabetic"

@app.route("/", methods=["GET", "POST"])
def diabetes_check():
    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])
        address = request.form["address"]
        illness_history = request.form["illness_history"]
        blood_sugar = int(request.form["blood_sugar"])
        result = check_diabetes(blood_sugar)

        return render_template("result.html", name=name, age=age, address=address, 
                               illness_history=illness_history, blood_sugar=blood_sugar, result=result)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
