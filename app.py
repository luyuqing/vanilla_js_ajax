import os
from flask import Flask, request, jsonify
from flask_cors import CORS


current_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=current_dir)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    output = ''
    if request.method == 'GET':

        # print(request.headers)
        # print(request.args)
        # print(request.form)
        # print(request.json)
        # print(request.data)

        token = request.headers.get('Bearer-Token')
        if token == '12345abced':
            name = request.args.get('name')
            age = request.args.get('age')
            output = f'Your name is {name} and you are {age} years old.'
    elif request.method == 'POST':
        token = request.headers.get('Bearer-Token')
        if token == '12345abced':
            content_type = request.headers.get('Content_type')
            # post form
            if content_type == 'application/x-www-form-urlencoded':
                name = request.form.get('name')
                age = request.form.get('age')
                output = {'name': name, 'age': age}
            # post json
            elif content_type == 'application/json':
                name = request.json.get('name')
                age = request.json.get('age')
                output = {'name': name, 'age': age}
            # post data, as coded in ajax4.html
            else:
                data = request.data.decode('utf-8')
                import json
                userInfo = json.loads(data)
                name = userInfo.get('name')
                age = userInfo.get('age')
                output = {'name': name, 'age': age}

    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)