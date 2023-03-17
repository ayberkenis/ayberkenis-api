from flask import Flask, render_template, jsonify, request

from core.ops import Downloader
from core.response import APIResponse

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
app.config['TEMPLATES_AUTO_RELOAD'] = True
d = Downloader()


@app.route('/')
def hello_world():
    """
    Render the index page
    :return:
    """
    return render_template('index.html')


@app.route('/api/v1/downloader/youtube/<identifier>', methods=['GET'])
def youtube(identifier):
    if request.method != 'GET':
        return jsonify(APIResponse(405, "Method not allowed").to_dict())
    quality, extension = request.args.get('quality'), request.args.get('extension')
    accepted_qualities = ['144p', '240p', '360p', '480p', '720p', '1080p', '1440p', '2160p', 'best']
    accepted_extensions = ['mp4', 'webm', 'mkv', 'flv', 'ogg', 'mp3', 'wav', 'aac', 'm4a', 'best']
    if quality and quality not in accepted_qualities:
        return jsonify(APIResponse(400, f"Invalid quality specified. Qualities accepted: {' | '.join(accepted_qualities)}").to_dict())

    if extension and extension not in accepted_extensions:
        return jsonify(APIResponse(400, f"Invalid extension specified. Extensions accepted: {' | '.join(accepted_extensions)}").to_dict())
    try:
        return d.youtube_downloader(identifier, quality, extension)
    except Exception as e:
        return jsonify(APIResponse(500, f"An error occurred while processing your request.", data={'error': str(e)}).to_dict())


@app.route('/api/v1/downloader/twitter/<identifier>', methods=['GET'])
def twitter(identifier):
    if request.method != 'GET':
        return jsonify(APIResponse(405, "Method not allowed").to_dict())
    # try:
    return d.twitter_downloader(identifier)
    # except Exception as e:
    #     return jsonify(APIResponse(500, f"An error occurred while processing your request.", data={'error': str(e)}).to_dict())

if __name__ == '__main__':
    app.run(debug=True)
