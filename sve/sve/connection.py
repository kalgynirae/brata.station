#TODO clean up imports
from sve.interfaces import IConnectionManager
from sve.state import HttpMethod
import json
import logging
import logging.handlers
import requests
import sys
from threading import Thread
from time import sleep
from time import time
from datetime import datetime
import traceback
from flask import Flask
from flask import request
from flask import jsonify
## TODO Delete
#import pprint
#TODO Delete from gevent import pywsgi
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import httplib
from sve.state import State


# ------------------------------------------------------------------------------
class ConnectionManager(IConnectionManager):

   _app = Flask(__name__)
   _callback = None


   # ---------------------------------------------------------------------------
   def __init__(self,
                sve,
                config):

      # TODO?
      """
   def __init__(self,
                todoHandler,
                config):
      """

      logger.debug('Constructing connection manager')
      logger.debug('Flask debugging? %s' % (self._app.config['DEBUG']))
      logger.debug('Flask testing? %s' % (self._app.config['TESTING']))
      logger.debug('Flask logger? %s' % (self._app.config['LOGGER_NAME']))
      logger.debug('Flask server? %s' % (self._app.config['SERVER_NAME']))
      self._connectUrl = config.ConnectUrl
      self._disconnectUrl = config.DisconnectUrl
      self._timeExpiredUrl = config.TimeExpiredUrl
      self._stationType = config.StationType
      self._stationInstanceId = config.StationInstanceId
      self._connected = False
      self._listening = False
      self._timeToExit = False

      self._callback = sve
      #TODO? self._handler = todoHandler

      self._app.add_url_rule('/station/1.0.0/reset',
                             'reset',
                             self.reset,
                             methods=['POST'])
      self._app.add_url_rule('/station/1.0.0/activate',
                             'activate',
                             self.activate,
                             methods=['POST'])
      self._app.add_url_rule('/station/1.0.0/submit',
                             'submit',
                             self.submit,
                             methods=['POST'])

      self._thread = Thread(target = self.run)
      self._thread.daemon = True
      self._thread.start()

   # ---------------------------------------------------------------------------
   @property
   def _connected(self):
      return self._connectedValue

   @_connected.setter
   def _connected(self,
                  value):
      self._connectedValue = value
      logger.info('Is connection manager connected? %s' % (value))

   # ---------------------------------------------------------------------------
   def __enter__(self):
      logger.debug('Entering connection manager')
      return self

   # ---------------------------------------------------------------------------
   def __exit__(self, type, value, traceback):
      logger.debug('Exiting connection manager')
      stopListening(self)
      self._timeToExit = True
      self._thread.join()

   # ---------------------------------------------------------------------------
   def run(self):
      logger.debug('Starting TODO thread for connection manager')

      while not self._timeToExit:
         try:
            if self._listening:

               if (not self._connected):
                  self.connect()
                  self._connected = True

                  # TODO named constant
                  port = 5000
                  # TODO Delete Disabled due to monkey seg fault on Raspbian
                  #TODO Delete server = pywsgi.WSGIServer(('', port), self._app)
                  #TODO Delete server.serve_forever()
                  server = HTTPServer(WSGIContainer(self._app))
                  server.listen(port)
                  IOLoop.instance().start()
               # TODO
               #pass

            sleep(1)
         except requests.ConnectionError, e:
            logging.critical(str(e))
            # TODO nothing to do - cannot connect because remote end is not up;
            # just wait and try again later
            # TODO configurable sleep time...
            sleep(3)
         except Exception, e:
            exType, ex, tb = sys.exc_info()
            logging.critical("Exception occurred of type " + exType.__name__)
            logging.critical(str(e))
            traceback.print_tb(tb)

      self.disconnect()

   # ---------------------------------------------------------------------------
   def startListening(self):
      logger.debug('Starting listening for connection manager')
      # TODO
      self._listening = True

   # ---------------------------------------------------------------------------
   def stopListening(self):
      logger.debug('Stopping listening for connection manager')
      self._listening = False
      self._connected = False


   # ---------------------------------------------------------------------------
   def getTimestamp(self):
      ts = time()
      st = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
      return st


   # ---------------------------------------------------------------------------
   def callService(self,
                   httpMethod,
                   endpointUrl,
                   args):
      args['message_timestamp'] = self.getTimestamp()
      logger.debug('Calling service with HTTP method %s, endpoint URL %s, and args %s' % (httpMethod, endpointUrl, args))
      data = json.dumps(args)
      response = requests.post(endpointUrl, data)

      # TODO Delete
      ##response = requests.post(endpointUrl, data, auth=('user', '*****'))

      # TODO Delete
      ##logger.debug('Service response: %s' % (response))
      ##logger.debug('Service response: %s' % (vars(response)))
      ##pprint.pprint(vars(response))
      ##logger.debug('Service response.text: %s' % (response.text))
      #logger.debug('Service response status_code: %s' % (response.status_code))
      #logger.debug('Service response.name1: %s' % (response.json['name1']))
      #logger.debug('Service response.name2: %s' % (response.json['name2']))

      logger.debug('Service returned %s for HTTP method %s, endpoint URL %s, and args %s' % (response.status_code, httpMethod, endpointUrl, args))
      return (response.status_code, response.json)


   # ---------------------------------------------------------------------------
   # TODO Delete @_app.route('/station/1.0.0/reset', methods=['POST'])
   def reset(self):

      # TODO...
      if not request.json:
      #if not request.json or not 'title' in request.json:
         #TODO abort(400)
         logger.debug('return 400?')

      # TODO - To test:
      # $ curl -X POST --header 'Content-Type: application/json' --data '{"message_version": 0, "message_timestamp": "2014-09-15 14:08:59", "PIN": "13579"}' 'http://localhost:5000/station/1.0.0/reset'

      message_version = request.json['message_version']
      message_timestamp = request.json['message_timestamp']
      pin = request.json['PIN']

      # TODO Delete
      #'title': request.json['title'],
      #'description': request.json.get('description', ""),

      logger.debug('Master server requesting station reset (ver %s) at %s with pin "%s"' % (message_version, message_timestamp, pin))

      # TODO implement method body
      self._callback.State = State.READY

      # TODO can't pass-in self - how to get handle to self? is it needed?

      # TODO
      resp = jsonify({'foo': 'bar'})
      resp.status_code = 200
      return resp


   # ---------------------------------------------------------------------------
   # TODO: Delete @_app.route('/station/1.0.0/activate', methods=['POST'])
   def activate(self):

      # TODO...
      if not request.json:
      #if not request.json or not 'title' in request.json:
         #TODO abort(400)
         logger.debug('return 400?')

      # TODO - To test:
      # $ curl -X POST --header 'Content-Type: application/json' --data '{"message_version": 0, "message_timestamp": "2014-09-15 14:08:59"}' 'http://localhost:5000/station/1.0.0/activate'

      message_version = request.json['message_version']
      message_timestamp = request.json['message_timestamp']

      # TODO Delete
      #'title': request.json['title'],
      #'description': request.json.get('description', ""),

      logger.debug('Master server requesting station activate (ver %s) at %s' % (message_version, message_timestamp))

      # TODO implement method body
      self._callback.State = State.PROCESSING

      # TODO can't pass-in self - how to get handle to self? is it needed?

      # TODO
      resp = jsonify({'foo': 'bar'})
      resp.status_code = 200
      return resp



   # ---------------------------------------------------------------------------
   # TODO: Delete @_app.route('/station/1.0.0/submit', methods=['POST'])
   def submit(self):

      # TODO...
      if not request.json:
      #if not request.json or not 'title' in request.json:
         #TODO abort(400)
         logger.debug('return 400?')

      # TODO - To test:
      # $ curl -X POST --header 'Content-Type: application/json' --data '{"message_version": 0, "message_timestamp": "2014-09-15 14:08:59", "submitted_answer": "42", "is_correct": "True"}' 'http://localhost:5000/station/1.0.0/submit'

      message_version = request.json['message_version']
      message_timestamp = request.json['message_timestamp']
      submitted_answer = request.json['submitted_answer']
      is_correct = request.json['is_correct']

      # TODO Delete
      #'title': request.json['title'],
      #'description': request.json.get('description', ""),

      logger.debug('Master server submitting (ver %s) user answer to station at %s. Answer "%s" is correct? %s' % (message_version, message_timestamp, submitted_answer, is_correct))

      # TODO implement method body
      if True: # TODO
         self._callback.State = State.PASSED

      # TODO can't pass-in self - how to get handle to self? is it needed?

      # TODO
      resp = jsonify({'foo': 'bar'})
      resp.status_code = 200
      return resp


   # ---------------------------------------------------------------------------
   def connect(self):
      logger.debug('Station requesting connect with master server')
      (status, response) = self.callService(
         HttpMethod.POST, self._connectUrl,
         {'message_version':     0,
          'station_instance_id': self._stationInstanceId,
          'station_type':        self._stationType,
          'station_host':        'todo_localhost',
          'station_port':        'todo_5000'})

      if status == httplib.OK:
         logger.debug('Service %s returned OK' % (self._connectUrl))
      elif status == httplib.NOT_FOUND:
         logger.debug('Service %s returned NOT_FOUND' % (self._connectUrl))
      else:
         logger.critical('Unexpected HTTP response %s received from service %s' % (status, self._connectUrl))


   # ---------------------------------------------------------------------------
   def disconnect(self):
      logger.debug('Station requesting disconnect from master server')
      (status, response) = self.callService(
         HttpMethod.POST, self._disconnectUrl,
         {'message_version':     0,
          'station_instance_id': self._stationInstanceId})


   # ---------------------------------------------------------------------------
   def timeExpired(self):
      logger.debug('Station informing master server that time for challenge has expired')

      self._callback.State = State.FAILED

      (status, response) = self.callService(
         HttpMethod.POST, self._timeExpiredUrl,
         {'message_version':     0,
          'station_instance_id': self._stationInstanceId})


# ------------------------------------------------------------------------------
# Module Initialization
# ------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # TODO - delete
handler = logging.handlers.SysLogHandler(address = '/dev/log')
logger.addHandler(handler)
