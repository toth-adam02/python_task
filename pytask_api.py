from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources import Applications, GlobalApplications, OrgApplications

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

api.add_resource(Applications, '/applications')
api.add_resource(GlobalApplications, '/global-applications')
api.add_resource(OrgApplications, '/org-applications')

if __name__ == '__main__':
    app.run(debug=True)