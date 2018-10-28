import json
import os
#import pyparticle as pp
from flask import Flask, request
app = Flask(__name__)
access_token = os.getenv('PARTICLE_ACCESS_TOKEN', '')
#particle = pp.Particle(access_token=os.getenv('PARTICLE_ACCESS_TOKEN', ''))

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/camera', methods=['GET'])
def hello_heidi():
    user = request.args.get('user')
    device_id = request.args.get('device_id')
    object_detected = request.args.get('object_detected')
    access_token = request.args.get('access_token')
    print(user)
    return json.dumps({
        'user': user,
        'device_id': device_id,
        'object_detected': object_detected,
        'access_token': access_token
        }, indent=2)
