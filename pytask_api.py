import csv
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

def read_csv(filename, limit, offset):
    with open(filename) as file:
        l = []
        reader = csv.reader(file)
        dreader = csv.DictReader(file, next(reader))
        for i in range(offset):
            next(dreader)
        for i in range(limit):
            l.append(next(dreader))
        return l

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('limit', type=int, location='args', default=0)
parser.add_argument('offset', type=int, location='args', default=0)

class Applications(Resource):
    def get(self):
        try:
            args = parser.parse_args()
            return read_csv("amp_tables/amp_applications.csv", args['limit'], args['offset'])
        except:
            return 'Server Error', 500

class GlobalApplications(Resource):
    def get(self):
        try:
            args = parser.parse_args()
            return read_csv("amp_tables/amp_global_applications.csv", args['limit'], args['offset'])
        except:
            return 'Server Error', 500

class OrgApplications(Resource):
    def get(self):
        try:
            args = parser.parse_args()
            return read_csv("amp_tables/amp_organization_applications.csv", args['limit'], args['offset'])
        except:
            return 'Server Error', 500

api.add_resource(Applications, '/applications')
api.add_resource(GlobalApplications, '/global-applications')
api.add_resource(OrgApplications, '/org-applications')

if __name__ == '__main__':
    app.run(debug=True)