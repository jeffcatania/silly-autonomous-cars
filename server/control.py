import time

class Control:
    lock = False

    def process_request(self, req):
        print(self.lock)
        if self.lock:
            return {
                'status': 'failure',
		'request': req
            }
        else:
            self.lock = True
#            time.sleep(5)
            self.lock = False
            return {
                'status': 'success',
		'request': req
            }
