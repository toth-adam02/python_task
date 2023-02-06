from flask_restful import Resource, reqparse
from csv_parser import read_csv

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