from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    a = int(request.form['a'])
    b = int(request.form['b'])
    c = a + b 
    return f"{a} + {b} = {c}"

if __name__ == '__main__':
    app.run(debug=True)
