from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    income = int(request.form['income'])
    expenses = int(request.form['expenses'])
    savings = income - expenses

    # Emergency fund
    emergency = expenses * 6

    # Basic advice
    if savings > 10000:
        advice = "Good saving habit"
    else:
        advice = "Try to reduce expenses"

    return render_template('result.html',
                           income=income,
                           expenses=expenses,
                           savings=savings,
                           emergency=emergency,
                           advice=advice)

if __name__ == '__main__':
    app.run(debug=True)
