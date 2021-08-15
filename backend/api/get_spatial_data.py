import numpy as np
from flask import Blueprint, jsonify
from flask_restx import Resource, Api, reqparse
import psycopg2
import pickle

conn = psycopg2.connect("dbname=st_kidney user=postgres password=0914040271qq")
cursor = conn.cursor()

API_VERSION_V1 = 1

api_bp = Blueprint('api', __name__)
api_v1 = Api(api_bp)

parser = reqparse.RequestParser()


class getSpatialPlotyVue(Resource):

    def get(self):

        cursor.execute("SELECT imagecol, imagerow FROM observation ORDER BY obs_id")
        data = cursor.fetchall()
        x,y = [],[]

        for i,j in data:
            x.append(i)
            y.append(j)
        return jsonify(
            [
                {
                    'x': x,
                    'y': y,
                    
                    'mode': 'markers',
                    'marker': {
                        'size': 5,
                        'color': []
                        },
                    
                    'hovertemplate': '<i>Gene count</i>: %{marker.color:.2f}',
                }
            ]
        )


api_v1.add_resource(getSpatialPlotyVue, '/sin')
