import logging
import logging.handlers
from station.interfaces import IStation


# ------------------------------------------------------------------------------
class Station(IStation):

   # ---------------------------------------------------------------------------
   def __init__(self,
                config,
                hwModule):
      logger.debug('Constructing CPA')

      # TODO - Jaron add code here

   # ---------------------------------------------------------------------------
   def start(self):
      logger.info('Starting CPA.')

      # TODO - Jaron add code here

   # ---------------------------------------------------------------------------
   def stop(self, signal):
      logger.info('Received signal "%s". Stopping CPA.', signal)

      # TODO - Jaron add code here

   # ---------------------------------------------------------------------------
   def onReady(self):
      logger.info('CPA transitioned to Ready state.')

      # TODO - Jaron add code here

   # ---------------------------------------------------------------------------
   def onProcessing(self):
      logger.info('CPA transitioned to Processing state.')

      # TODO - Jaron add code here

   # ---------------------------------------------------------------------------
   def onFailed(self):
      logger.info('CPA transitioned to Failed state.')

      # TODO - Jaron add code here

   # ---------------------------------------------------------------------------
   def onPassed(self):
      logger.info('CPA transitioned to Passed state.')

      # TODO - Jaron add code here

   # ---------------------------------------------------------------------------
   def onUnexpectedState(self, value):
      logger.critical('CPA transitioned to Unexpected state %s', value)

      # TODO - Jaron add code here


# ------------------------------------------------------------------------------
# Module Initialization
# ------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # TODO - delete
handler = logging.handlers.SysLogHandler(address = '/dev/log')
logger.addHandler(handler)

