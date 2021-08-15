import numpy as np
from flask import Blueprint, jsonify
from flask_restx import Resource, Api, reqparse
import psycopg2
import pickle

conn = psycopg2.connect("dbname=st_kidney user=postgres password=0914040271qq")
cursor = conn.cursor()

API_VERSION_V1 = 1

api_gc = Blueprint('apigc', __name__)
api_v1 = Api(api_gc)

parser = reqparse.RequestParser()


class getGeneCount(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('gene', type=str, help='Gene_name')
        args = parser.parse_args()
  

        uuid = args.gene
        cursor.execute(
            """
            SELECT var_expression
            FROM variable
            WHERE var_name=%s
            """,
            (uuid,)
        )
        some_array = pickle.loads(cursor.fetchone()[0])

        return jsonify(
            [
                {
                    "gene_count": some_array.tolist()

                }
            ]
        )


api_v1.add_resource(getGeneCount, '/getGeneCount')
