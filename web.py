import flask
from flask import request, jsonify, render_template, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False
from modules import earthquake as ea
from modules import exchange as ex
from datetime import datetime

limiter = Limiter(app, key_func=get_remote_address, default_limits=["200 per hour", "50 per minute"])



@app.route('/', methods=['GET'])
def home():
    dt = datetime.utcnow()
    return render_template("index.html", dt=dt)

@app.route('/v1/earthquakes/latest', methods=['GET'])
def latest_index():
    return jsonify(ea.deprem_latest())

@app.route('/v1/earthquakes/all', methods=['GET'])
def all_index():
    return jsonify(ea.deprem_all())

@app.route('/v1/earthquakes', methods=['GET'])
def query_index():
    return jsonify(ea.deprem_query())

@app.route('/v1/earthquakes_api', methods=['GET'])
def deprem_landing():
    return render_template("earthquakes.html")



@app.route("/v1/exchanges/", methods=["GET"])
def exchange_all():
    return jsonify(ex.exchange_all())

@app.route("/v1/exchange", methods=["GET"])
def exchange_query():
    return jsonify(ex.exchange_query())

@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(jsonify(error=f"you're being rate limited. Rate limit you exceeded: {e.description}. Contact api@ayberkenis.online"), 429)


app.run()