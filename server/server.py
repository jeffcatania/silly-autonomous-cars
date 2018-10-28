import json
import os
import pyparticle as pp
from flask import Flask, request

from server.control import Control

c = Control()

app = Flask(__name__)
access_token = os.getenv('PARTICLE_ACCESS_TOKEN', '')
particle = pp.Particle(access_token=os.getenv('PARTICLE_ACCESS_TOKEN', ''))

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/camera', methods=['GET'])
def hello_heidi():
    device_id = request.args.get('device_id')
    object_state = request.args.get('state')
    r = c.process_request({
	'device_id': device_id,
	'state': object_state
    })
    #particle_result = particle.call_function(device_id, 'led', 'off')
    return json.dumps({
        'response': r
        }, indent=2)
