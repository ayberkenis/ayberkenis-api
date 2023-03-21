from flask import Flask, render_template, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from core.exceptions import YoutubeVideoNotAvailable, TwitterVideoNotAvailable, TwitterAPIError, InstagramAPIError, \
    InstagramVideoNotAvailable, TiktokVideoNotAvailable
from core.ops import Downloader
from core.response import APIResponse

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "1 per second"],
    storage_uri="memory://",
    strategy="fixed-window",
)

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
@limiter.limit("1 per second")
def youtube(identifier):
    """
    Endpoint for downloading a YouTube video
    Args:
        identifier:

    Returns:

    """
    if request.method != 'GET':
        return jsonify(APIResponse(405, "Method not allowed").to_dict())
    quality, extension = request.args.get('quality'), request.args.get('extension')
    accepted_qualities = ['144p', '240p', '360p', '480p', '720p', '1080p', '1440p', '2160p', 'best']
    accepted_extensions = ['mp4', 'webm', 'mkv', 'flv', 'ogg', 'mp3', 'wav', 'aac', 'm4a', 'best']
    if quality and quality not in accepted_qualities:
        return jsonify(APIResponse(400, f"Invalid quality specified. Qualities accepted: {' | '.join(accepted_qualities)}").to_dict())

    if extension and extension not in accepted_extensions:
        return jsonify(APIResponse(400, f"Invalid extension specified. Extensions accepted: {' | '.join(accepted_extensions)}").to_dict())

    return d.youtube_downloader(identifier, quality, extension)


@app.route('/api/v1/downloader/twitter/<identifier>', methods=['GET'])
@limiter.limit("1 per second")
def twitter(identifier):
    """
    Endpoint for downloading a Twitter video
    Args:
        identifier:

    Returns:

    """
    print('twitter route?')
    print(request.data)
    return d.twitter_downloader(identifier)

@app.route('/api/v1/downloader/instagram/<type>/<identifier>', methods=['GET'])
@limiter.limit("1 per second")
def instagram(type, identifier):
    """
    Endpoint for downloading an Instagram video
    Args:
        identifier:

    Returns:

    """
    return d.instagram_downloader(identifier, type)

@app.route('/api/v1/downloader/tiktok/<identifier>', methods=['GET'])
@limiter.limit("1 per second")
def tiktok(identifier):
    """
    Endpoint for downloading a Tiktok video
    Args:
        identifier:

    Returns:

    """
    return d.tiktok_downloader(identifier)

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors
    Args:
        e:

    Returns:

    """
    return jsonify(APIResponse(500, "Internal server error", data={'error': str(e)}).to_dict()), 500

@app.errorhandler(405)
def internal_server_error(e):
    """
    Handle 500 errors
    Args:
        e:

    Returns:

    """
    return jsonify(APIResponse(405, "Internal server error", data={'error': str(e)}).to_dict()), 405

@app.errorhandler(YoutubeVideoNotAvailable)
def youtube_video_not_available(e):
    """
    Handle 500 errors
    Args:
        e:

    Returns:

    """
    return jsonify(APIResponse(404, "Youtube video not available", data={'error': str(e)}).to_dict()), 404

@app.errorhandler(TwitterVideoNotAvailable)
def twitter_video_not_available(e):
    """
    Handle 500 errors
    Args:
        e:

    Returns:

    """
    return jsonify(APIResponse(404, "Twitter video not available", data={'error': str(e)}).to_dict()), 404

@app.errorhandler(TwitterAPIError)
def twitter_api_error(e):
    """
    Handle 500 errors
    Args:
        e:

    Returns:

    """
    return jsonify(APIResponse(500, "Twitter API error", data={'error': str(e)}).to_dict()), 500

@app.errorhandler(InstagramAPIError)
def instagram_api_error(e):
    """
    Handle 500 errors
    Args:
        e:

    Returns:

    """
    return jsonify(APIResponse(500, "Instagram API error", data={'error': str(e)}).to_dict()), 500

@app.errorhandler(InstagramVideoNotAvailable)
def instagram_video_not_available(e):
    """
    Handle 500 errors
    Args:
        e:

    Returns:

    """
    return jsonify(APIResponse(404, "Instagram video not available", data={'error': str(e)}).to_dict()), 404

@app.errorhandler(TiktokVideoNotAvailable)
def tiktok_video_not_available(e):
    """
    Handle 500 errors
    Args:
        e:

    Returns:

    """
    return jsonify(APIResponse(404, "Tiktok video not available", data={'error': str(e)}).to_dict()), 404




if __name__ == '__main__':
    app.run(debug=True)
