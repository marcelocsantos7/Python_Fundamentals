#!usr/bin/python3

import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])

def homePage():
    dados ={
        'API' : 'Python',
        'Dado' : 'Pythons é melhor que PHP'
    }
    return flask.jsonify(dados)
    # return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)