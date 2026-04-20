from flask import Flask, make_response

app = Flask(__name__)

customers = ["bob", "john"]

contracts = {
    1: "This contract is for John and building a shed",
    2: "This contract is for Bob and painting a house"
}

@app.route("/")
def index():
    return "Welcome to Contracts API"


@app.route("/contract/<int:contract_id>")
def get_contract(contract_id):
    if contract_id in contracts:
        return contracts[contract_id], 200
    return make_response("Contract not found", 404)


@app.route("/customer/<string:name>")
def get_customer(customer_name):
    if customer_name.lower() in customers:
        return "", 204
    return make_response("Customer not found", 404)

if __name__ == "__main__":
    app.run(debug=True)
