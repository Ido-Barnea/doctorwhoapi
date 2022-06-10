from flask import *
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    return render_template('help.html')

@app.errorhandler(404)
def not_found_page(e):
    return f'Error: The page was not found.'

@app.route('/images/<image_id>', methods=['GET'])
def images_page(image_id):
    if image_id is None:
        return 'Expected id.'
    else:
        try:
            return send_file('images\\' + image_id + '.png', mimetype='image/png')
        except FileNotFoundError:
            return f'The image "{image_id}" was not found.'

def get_data(file_name, data_id):
    with open(f'data/{file_name}.json', 'r') as f:
        data = json.load(f)

    if data_id is None:
        return str(data)
    else:
        try:
            index = data_id - 1
            return str(data[index])
        except ValueError:
            return 'Index must be an integer.'
        except IndexError:
            return 'Index out of range.'

@app.route('/doctors/', defaults={'doctor_id': None}, methods=['GET'])
@app.route('/doctors/<int:doctor_id>', methods=['GET'])
def doctors_page(doctor_id):
    return get_data('doctors', doctor_id)

@app.route('/companions/', defaults={'companion_id': None}, methods=['GET'])
@app.route('/companions/<int:companion_id>', methods=['GET'])
def companions_page(companion_id):
    return get_data('companions', companion_id)

@app.route('/actors/', defaults={'actor_id': None}, methods=['GET'])
@app.route('/actors/<int:actor_id>', methods=['GET'])
def actors_page(actor_id):
    return get_data('actors', actor_id)

@app.route('/writers/', defaults={'writer_id': None}, methods=['GET'])
@app.route('/writers/<int:writer_id>', methods=['GET'])
def writers_page(writer_id):
    return get_data('writers', writer_id)


if __name__ == '__main__':
    app.run(port=4444)
