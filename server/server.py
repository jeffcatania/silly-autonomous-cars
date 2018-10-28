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
    user = request.args.get('user')
    device_id = request.args.get('device_id')
    object_detected = request.args.get('object_detected')
    access_token = request.args.get('access_token')
    devices = particle.list_devices()
    print('Found %d device(s)' % len(devices))
    print(user)
    r = c.process_request(3)
    #particle_result = particle.call_function(device_id, 'led', 'off')
    #print('Water plant result: %s' % water_planet_result['return_value'])
    return json.dumps({
        'user': user,
        'device_id': device_id,
        'object_detected': object_detected,
        'access_token': access_token,
        #'particle_result': particle_result,
        'r': r
        }, indent=2)
