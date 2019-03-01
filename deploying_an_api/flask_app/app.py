from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/add", methods=['GET', 'POST'])
def predict():
    input1 = request.args.get('input1')
    input2 = request.args.get('input2')
    append = input1 + input2
    sum = float(input1) + float(input2)
    d = {'sum': sum, 'append': append}
    return jsonify(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)