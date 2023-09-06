from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def calculate():
    result = 0

    if request.method == 'POST':
        x = float(request.form['x'])
        y = float(request.form['y'])
        operator = request.form['operator']

        if operator == 'add':
            result = x + y
        elif operator == "subtract":
            result = x - y
        elif operator == "multiply":
            result = x * y
        elif operator == "divide":
            if y == 0:
                return "ERROR: Division by 0"
            result = x / y
        else:
            return "Please choose a valid operator"

        return "Result: " + str(result)
    
    return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
