from flask import Flask, request  # constructor

app = Flask(__name__)

@app.route("/") #default - GET method
def home(): 
    return "Hello from Flask!"

@app.route("/contact")
def contact():
    return "Contact me on example@gmail.com"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return "You are in GET method"
    else:
        data = request.get_json()
        if not data:
            return f"Data not entered"

        name = data.get('name')
        age = data.get('age')
        return f"Username: {name}, Age: {age}"


if __name__ == "__main__":

    app.run(debug=True)