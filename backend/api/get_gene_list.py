import numpy as np
from flask import Blueprint, jsonify
from flask_restx import Resource, Api, reqparse
import psycopg2

conn = psycopg2.connect("dbname=st_kidney user=postgres password=0914040271qq")
cursor = conn.cursor()

API_VERSION_V1 = 1

api_gl = Blueprint('getgene', __name__)
api_v1 = Api(api_gl)

parser = reqparse.RequestParser()


class getGeneListVue(Resource):

    def get(self):

        cursor.execute("SELECT var_name FROM variable ORDER BY var_id")
        tmp = cursor.fetchall()

        gene_names = []
        for gene in tmp:
            gene_names.append(gene[0])

        return jsonify(
            [
                {
                    'gene_names': gene_names,
                }
            ]
        )


api_v1.add_resource(getGeneListVue, '/getGeneList')
