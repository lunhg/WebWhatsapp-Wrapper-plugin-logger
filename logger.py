import os
import json

# Logger utility for lunhg/WebWhatsapp-Wrapper
# Usage
# logger = Logger(logdir=</logdir>)
class Logger(object):

  def __init__(self, **kwargs):
    self.driver = kwargs.get('driver')

  def setup(self, **kwargs):
    # Wheres log
    self.logdir = kwargs.get('logdir')
    log = os.path.join(self.logdir, 'log.json')
    self.logfh = open(log, "a")
    if (self.logfh.tell() == 0):
      self.logfh.write('[]')
      self.logfh.flush()

   # Implement a handle function to be called on
   # lunhg/Webwhatsapp-Wrapper
   def handle(self, chat, message):
     msg = {
       'uid': chat.id,
       'msg': message.content,
       'tim': int(time.time()),
     }
     pos = self.logfh.tell()
     self.logfh.seek(pos-1)
     self.logfh.truncate()
     if (pos > 2):
       self.logfh.write(', ')
       self.logfh.write(json.dumps(msg))
       self.logfh.write(']')
       self.logfh.flush()
