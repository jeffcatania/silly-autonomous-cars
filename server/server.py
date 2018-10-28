import json
import os
from flask import Flask, request

from server.control import Control

c = Control()

app = Flask(__name__)
access_token = os.getenv('PARTICLE_ACCESS_TOKEN', '')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/start', methods=['GET'])
def start():
    r = c.process_start()
    return json.dumps({
        'response': r
        }, indent=2)

@app.route('/api/stop', methods=['GET'])
def stop():
    r = c.process_stop()
    return json.dumps({
        'response': r
        }, indent=2)

@app.route('/api/camera', methods=['GET'])
def camera():
    device_id = request.args.get('device_id')
    state = request.args.get('state')
    r = c.process_request({
	'device_id': device_id,
	'state': state
    })
    return json.dumps({
        'response': r
        }, indent=2)
