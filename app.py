from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define functions for add and multiply operations
def add(operand1, operand2):
    return operand1 + operand2

def multiply(operand1, operand2):
    return operand1 * operand2

# Define a route to handle the calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    operand1 = float(request.form['operand1'])
    operator = request.form['operator']
    operand2 = float(request.form['operand2'])

    result = None
    error_message = None

    try:
        if operator == '+':
            result = add(operand1, operand2)
        elif operator == '*':
            result = multiply(operand1, operand2)
        elif operator == '-':
            # For subtraction, you can implement a sub function if needed
            pass
        elif operator == '/':
            if operand2 != 0:
                # For division, you can implement a div function if needed
                pass
            else:
                error_message = 'Error: Division by zero'
        else:
            error_message = 'Error: Invalid operator'
    except Exception as e:
        error_message = f'Error: {str(e)}'

    return render_template('index.html', result=result, error_message=error_message)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
