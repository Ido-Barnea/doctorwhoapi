from flask import *
import json
from IMDBUtil import IMDBUtil

app = Flask(__name__)
imdb = IMDBUtil()

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
        return data
    else:
        try:
            index = data_id - 1
            return data[index]
        except ValueError:
            return 'Index must be an integer.'
        except IndexError:
            return 'Index out of range.'

@app.route('/doctors/', defaults={'doctor_id': None}, methods=['GET'])
@app.route('/doctors/<int:doctor_id>', methods=['GET'])
def doctors_page(doctor_id):
    return str(get_data('doctors', doctor_id))

@app.route('/companions/', defaults={'companion_id': None}, methods=['GET'])
@app.route('/companions/<int:companion_id>', methods=['GET'])
def companions_page(companion_id):
    return str(get_data('companions', companion_id))

@app.route('/actors/', defaults={'actor_id': None}, methods=['GET'])
@app.route('/actors/<int:actor_id>', methods=['GET'])
def actors_page(actor_id):
    actor_data = get_data('actors', actor_id)
    if actor_id is None:
        return str(actor_data)
    else:
        imdb_actor_data = imdb.get_actor(actor_data.get('name'))
        actor_data.update(imdb_actor_data)
        return actor_data

@app.route('/writers/', defaults={'writer_id': None}, methods=['GET'])
@app.route('/writers/<int:writer_id>', methods=['GET'])
def writers_page(writer_id):
    return str(get_data('writers', writer_id))

@app.route('/plot-outline', methods=['GET'])
def plot_outline():
    return 'The Doctor, a Time Lord from the race whose home planet is Gallifrey,' \
           'travels through time and space in their ship the TARDIS (an acronym for Time and Relative Dimension In Space) with numerous companions.' \
           'From time to time, the Doctor regenerates into a new form.'

@app.route('/cover-url', methods=['GET'])
def cover_url():
    return imdb.get_cover_url()

@app.route('/rating', methods=['GET'])
def rating():
    return imdb.get_rating()


if __name__ == '__main__':
    app.run(port=4444)
