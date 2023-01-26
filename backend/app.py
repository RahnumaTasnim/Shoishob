from flask import Flask, request
from flask_restful import Resource, Api
import pickle
import numpy as np

model = pickle.load(open('./model/model_file.pkl', 'rb'))

app = Flask(__name__)
api = Api(app)

class PredictExpertise(Resource):
    def post(self):
        json_data = request.json
        value_array = json_data['value_array']
        ans = value_array.split(',')
        print(ans)
        X_new = np.array([ans])
        result = model.predict(X_new)[0]
        print(result)
        # print('updated')
        return {'level': result}

api.add_resource(PredictExpertise, '/')

if __name__ == '__main__':
    # print('here')
    app.run(host='0.0.0.0', debug=True)