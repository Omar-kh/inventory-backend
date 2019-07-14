from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)
api = Api(app)


class Inventory(Resource):
    def get(self):
        df = pd.read_csv("products.csv", index_col="product_id")
        df.drop("Unnamed: 0", axis=1, inplace=True)
        data = [{"product_id": idx, "product_name": df.loc[idx, "product_name"]}
                for idx in df.index]
        return data


class Product(Resource):
    def get(self, product_id):
        df = pd.read_csv("inventory.csv", index_col="Unnamed: 0")
        df2 = pd.read_csv("products.csv", index_col="product_id")
        values = list(df.loc[product_id, :])
        dates = list(df.columns)
        product_name = df2.loc[product_id, "product_name"]
        data = {
            "product_id": product_id,
            "product_name": product_name,
            "dates": dates,
            "values": values
        }
        return data

    def put(self, product_id):
        received_request = request.get_json()
        product = received_request["data"]
        df = pd.read_csv("inventory.csv", index_col="Unnamed: 0")
        df.loc[product_id, :] = product["values"]
        df.to_csv("inventory.csv")


api.add_resource(Inventory, '/inventory')
api.add_resource(Product, '/inventory/<string:product_id>')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
