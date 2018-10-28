import time
import pyparticle as pp
import os

class Control:
    particle = pp.Particle(access_token=os.getenv('PARTICLE_ACCESS_TOKEN', ''))
    lock = False 

    def process_start(self):
       pass
#       res = self.particle.call_function('3d0024000c47353136383631', 'power', 'on')

    def process_stop(self):
       pass
#       res = self.particle.call_function('3d0024000c47353136383631', 'power', 'off')
	

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
               try:
                   res = self.particle.call_function('3d0024000c47353136383631', 'dir', 'right')
               except Exception as e:
                   print(e)
            self.lock = False
            return {
                'status': 'success',
		'request': req,
                'response': res
            }
