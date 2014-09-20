from importlib import import_module
import logging
import logging.handlers
# TODO - Is the ILed import needed?
from sve.interfaces import ILed
from sve.state import State
from threading import Thread
import time


# ------------------------------------------------------------------------------
class Sve:

   # ---------------------------------------------------------------------------
   def __init__(self,
                config):
      logger.debug('Constructing SVE')

      hwModuleName = config.HardwareModuleName
      ledClassName = config.LedClassName
      vibrationMotorClassName = config.VibrationMotorClassName

      hwModule = import_module(hwModuleName)
      ledClass = getattr(hwModule, ledClassName)
      vibrationMotorClass = getattr(hwModule, vibrationMotorClassName)

      self._state = None
      self._vibrationMotors = []

      for i in config.VibrationMotors:
         self._vibrationMotors.append(
            VibrationManager(i.Name, i, vibrationMotorClass))

      self._leds = []

      for i in config.Leds:
         self._leds.append(
            ledClass(i.Name, i))

      connectionModuleName = config.ConnectionModuleName
      connectionManagerClassName = config.ConnectionManagerClassName

      connectionModule = import_module(connectionModuleName)
      connectionManagerClass = getattr(connectionModule,
                                       connectionManagerClassName)

      self._connectionManager = connectionManagerClass(config.ConnectionManager)


   # ---------------------------------------------------------------------------
   @property
   def State(self):
      return self._state

   @State.setter
   def State(self, value):
      self._state = value

      if value == State.READY:
         for motor in self._vibrationMotors:
            motor.stop()
         for led in self._leds:
            led.turnOff()
      elif value == State.PROCESSING:
         for motor in self._vibrationMotors:
            motor.start()
         for led in self._leds:
            led.turnOff()
         self._leds['yellow'].turnOn()
      elif value == State.FAILED:
         for motor in self._vibrationMotors:
            motor.stop()
         for led in self._leds:
            led.turnOff()
         self._leds['red'].turnOn()
      elif value == State.PASSED:
         for motor in self._vibrationMotors:
            motor.stop()
         for led in self._leds:
            led.turnOff()
         self._leds['green'].turnOn()
      else:
         logger.critical('Unexpected state %s encountered', value)
         for led in self._leds:
            led.setFlashing()

   @State.deleter
   def State(self):
      del self._state

   # ---------------------------------------------------------------------------
   def start(self):

      logger.info('Starting SVE.')

      self.State = State.READY

      self._connectionManager.startListening()

      while True:
         time.sleep(1)

   # ---------------------------------------------------------------------------
   def stop(self, signal):

      logger.info('Received signal "%s". Stopping SVE.', signal)

      for motor in self._vibrationMotors:
         motor.stop()

      self._connectionManager.stopListening()

   # ---------------------------------------------------------------------------
   def buttonPressed():

      if self.State == State.READY:
         newState = State.PROCESSING
      else:
         newState = State.READY

      logger.info('Button press received. Transitioning to %s state', newState)
      self.State = newState


# ------------------------------------------------------------------------------
class VibrationManager:

   # ---------------------------------------------------------------------------
   def __init__(self,
                name,
                config,
                vibrationMotorClass):
      self.Name = name
      logger.debug('Constructing vibration manager %s', self.Name)
      self._started = False
      self._timeToExit = False
      self.OnDuration_s = config.OnDuration_s
      self.OffDuration_s = config.OffDuration_s
      self._vibrationMotor = vibrationMotorClass(self.Name)
      self._thread = Thread(target = self.run)
      self._thread.daemon = True
      self._thread.start()

   # ---------------------------------------------------------------------------
   def __enter__(self):
      logger.debug('Entering vibration manager %s', self.Name)
      return self

   # ---------------------------------------------------------------------------
   def __exit__(self, type, value, traceback):
      logger.debug('Exiting vibration manager %s', self.Name)
      stopListening(self)
      self._timeToExit = True
      self._thread.join()

   # ---------------------------------------------------------------------------
   def run(self):
      # TODO: Delete? clean up imports?
      """
      logger.debug('Starting key press thread for push button')

      while not self._timeToExit:
         try:
            if self._started:

               # TODO
               pass

            sleep(1)
         except Exception, e:
            exType, ex, tb = sys.exc_info()
            logging.critical("Exception occurred of type " + exType.__name__)
            logging.critical(str(e))
            traceback.print_tb(tb)
      """


   # ---------------------------------------------------------------------------
   def start(self):
      logger.debug('Starting vibration manager %s', self.Name)
      self._started = True

   # ---------------------------------------------------------------------------
   def stop(self):
      logger.debug('Stopping vibration manager %s', self.Name)
      self._started = False


# ------------------------------------------------------------------------------
# Module Initialization
# ------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # TODO - delete
handler = logging.handlers.SysLogHandler(address = '/dev/log')
logger.addHandler(handler)
