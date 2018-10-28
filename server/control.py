import time
import pyparticle as pp
import os

class Control:
    particle = pp.Particle(access_token=os.getenv('PARTICLE_ACCESS_TOKEN', ''))
    lock = False 

    def process_start(self):
       res = self.particle.call_function('3d0024000c47353136383631', 'power', 'on')

    def process_stop(self):
       res = self.particle.call_function('3d0024000c47353136383631', 'power', 'off')
	

    def process_request(self, req):
        print(self.lock)
        if self.lock:
            return {
                'status': 'failure',
		'request': req
            }
        else:
            #self.lock = True
            res = {}
            if req['state'] == "true":
               res = self.particle.call_function('3d0024000c47353136383631', 'dir', 'right')
	  #particle_result = particle.call_function(device_id, 'led', 'off')
#            time.sleep(5)
            self.lock = False
            return {
                'status': 'success',
		'request': req,
                'response': res
            }
