from flask import Flask, make_response

app = Flask(__name__)

contract_information = {
    1: "This contract is for John and building a shed",
    2: "This contract is for Bob and painting a house"
}

customer_information = ["bob", "john"]

@app.route("/contract/<int:id>")
def contract(id):
    if id in contract_information:
        return contract_information[id], 200
    return make_response("Contract not found", 404)

@app.route("/customer/<string:customer_name>")
def customer(customer_name):
    if customer_name.lower() in customer_information:
        return "", 204
    return make_response("Customer not found", 404)

if __name__ == "__main__":
    app.run(debug=True)