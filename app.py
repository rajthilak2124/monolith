from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Karunya Monolithic App!"

@app.route("/products")
def products():
    return jsonify(["Laptop", "Mouse", "Keyboard"])

@app.route("/orders")
def orders():
    return jsonify(["Order#101", "Order#102"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
