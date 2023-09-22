from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd

app = Flask(__name__)
api = Api(app)

todos = {}
dataSource = pd.read_excel('MOCK_DATA.xlsx')
dataSource = dataSource.set_index('action_id').T.to_dict()

@app.route('/')
def hello_world():
    return '<p>Hello, World!!!!-1</p>'


@app.route('/about-us')
def about_us():
    return '<p>This is a demo site 1111'


class HelloWorldApi(Resource):
    def get(self):
        return {'status':'200', 'error':'false', 'data' : dataSource}
    
api.add_resource(HelloWorldApi,'/api/hello')


class TodoAppApi(Resource):
    def get(self, todo_id):
        # print(todos)
        return {'status':'200', 'error':'false', 'data' : todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        # print(todos)
        return {'status':'200', 'error':'false', 'data' : todos[todo_id]}


class GetAllTodos(Resource):
       def get(self):
        #    print(todos)
        return {'status':'200', 'error':'false', 'data' : todos}
       def demo (self):
            return {'status':'200', 'error':'false', 'data' : todos}

api.add_resource(TodoAppApi, '/api/todos/<string:todo_id>')
api.add_resource(GetAllTodos, '/api/todos')

if __name__=='__main__':
    app.run(debug=True)

