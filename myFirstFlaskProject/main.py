from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return '<p>Hello, World!!!!-1</p>'


@app.route('/about-us')
def about_us():
    return '<p>This is a demo site 1111'

class HelloWorldApi(Resource):
    def get(self):
        return {'status':'200', 'error':'false', 'message' : 'hello world!'}
    
api.add_resource(HelloWorldApi,'/api/hello')

if __name__=='__main__':
    app.run(debug=True)
