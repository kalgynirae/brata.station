# ------------------------------------------------------------------------------
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
#  See the License for the specific language governing permissions and
#  limitations under the License.
# ------------------------------------------------------------------------------
"""
TODO module description
"""

import logging
import logging.handlers
import pibrella
import signal
import sys
import traceback

from interfaces import IDisplay
from interfaces import ILed
from interfaces import IPushButton
from interfaces import IVibrationMotor


# ------------------------------------------------------------------------------
class Display(IDisplay):
    """
    TODO class comment
    """
    # TODO Reference the bottom of this for the code needed for the LCD display:
    # https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_CharLCDPlate/Adafruit_CharLCDPlate.py
    # TODO for text > 16 chars - might need to consider scrolling to display all the text

    # --------------------------------------------------------------------------
    def __init__(self,
                 config):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        logger.debug('Constructing display')

        self._line1Text = ''
        self._line2Text = ''

    # --------------------------------------------------------------------------
    def __enter__(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        logger.debug('Entering display')
        return self

    # --------------------------------------------------------------------------
    def __exit__(self, type, value, traceback):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        logger.debug('Exiting display')
        self.setText('')

    # --------------------------------------------------------------------------
    def setLine1Text(self,
                     text):
        """Sets the text for line 1 of the display.

        Sets the text for line 1 of the display. If the text is too long to fit
        on the display, then the text scrolls over time.

        Args:
            text (string): The text to display.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        self._line1Text = text
        # TODO
        logger.debug('Setting Line 1 text. Display now reads "%s"[br]"%s"' %
                     (self._line1Text, self._line2Text))


    # --------------------------------------------------------------------------
    def setLine2Text(self,
                     text):
        """Sets the text for line 2 of the display.

        Sets the text for line 2 of the display. If the text is too long to fit
        on the display, then the text scrolls over time.

        Args:
            text (string): The text to display.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        self._line2Text = text
        # TODO
        logger.debug('Setting Line 2 text. Display now reads "%s"[br]"%s"' %
                     (self._line1Text, self._line2Text))


    # --------------------------------------------------------------------------
    def setText(self,
                text):
        """Sets the text for the entire display.

        Directly sets the text for the display. Multiple lines can be provided
        at once by separating with a '\n' character.

        Args:
            text (string): The text to display.
        Returns:
            N/A.
        Raises:
            N/A.

        """
        idx = text.find('\n')

        if idx != -1:
            self._line1Text = text[:idx]
            self._line2Text = text[idx+1:]
        else:
            self._line1Text = text
            self._line2Text = ''

        # TODO
        logger.debug('Setting Line 2 text. Display now reads "%s"[br]"%s"' %
                     (self._line1Text, self._line2Text))


# ------------------------------------------------------------------------------
class Led(ILed):
    """
    TODO class comment
    """

    # --------------------------------------------------------------------------
    def __init__(self,
                 name, 
                 config):
        """Initializes the LED class

        TODO Detailed multi-line description if
        necessary.

        Args:
            name (string): Name of this instance of the LED class. Example "Bob"
            config (Config): Configuration object for the LED class
        Returns:
            N/A
        Raises:
            N/A

        """
        self.Name = name
        self.FlashingOnDuration_s = 0.5
        self.FlashingOffDuration_s = 0.5
        self.outputPin = getattr(pibrella.light, config.OutputPin)

    # --------------------------------------------------------------------------
    def turnOn(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        logger.debug('Set LED steady ON \"%s\".', self.Name)
        self.outputPin.on()

    # --------------------------------------------------------------------------
    def turnOff(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        logger.debug('Set LED steady OFF \"%s\".', self.Name)
        self.outputPin.off()

    # --------------------------------------------------------------------------
    def setFlashing(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        logger.debug('Set LED flashing \"%s (%s..%s)\".',
                     self.Name,
                     self.FlashingOnDuration_s,
                     self.FlashingOffDuration_s)
        
        # Pulse function, FadeInTime_s, FadeOutTime_s, OnTime_s, OffTime_s
        self.outputPin.pulse(0, 0, self.FlashingOnDuration_s, self.FlashingOffDuration_s);


# ------------------------------------------------------------------------------
class PushButton(IPushButton):
    """
    TODO class comment
    """
    # TODO Reference the bottom of this for the code needed for push buttons:
    # https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_CharLCDPlate/Adafruit_CharLCDPlate.py

    # --------------------------------------------------------------------------
    def __init__(self,
                 buttonPressHandler,
                 config):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        logger.debug('Constructing push button')
        self._listening = False
        self._timeToExit = False
        self._handler = buttonPressHandler
        self._thread = Thread(target = self.run)
        self._thread.daemon = True
        self._thread.start()

    # --------------------------------------------------------------------------
    def __enter__(self):
        logger.debug('Entering push button')
        return self

    # --------------------------------------------------------------------------
    def __exit__(self, type, value, traceback):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        logger.debug('Exiting push button')
        self.stopListening()
        self._timeToExit = True
        self._thread.join()

    # --------------------------------------------------------------------------
    def run(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        with NonBlockingConsole() as nbc:
            logger.debug('Starting key press thread for push button')

            while not self._timeToExit:
                try:
                    if self._listening:

                        # TODO
                        pass

                    sleep(1)
                except Exception, e:
                    # JIA TODO BEGIN change
                    #logger.critical("Exception occurred: " + e.args[0])
                    # JIA TODO UPDATE change
                    exType, ex, tb = sys.exc_info()
                    logger.critical("Exception occurred of type " + exType.__name_)
                    logger.critical(str(e))
                    traceback.print_tb(tb)
                    # JIA TODO END change

    # --------------------------------------------------------------------------
    def startListening(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        logger.debug('Starting listening for push button')
        # TODO
        self._listening = True

    # --------------------------------------------------------------------------
    def stopListening(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        logger.debug('Stopping listening for push button')
        self._listening = False


# ------------------------------------------------------------------------------
class VibrationMotor(IVibrationMotor):
    """
    TODO class comment
    """

    # --------------------------------------------------------------------------
    def __init__(self,
                 name,
                 outputPin):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            name (string): Name of this motor, example "Huey"
            outputPin (string): Letter Designation of Pin , "E", "F", "G", or"H"
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        self.Name = name
        #TODO - Need to get these from config file [SS]
        #self.OnDuration_s = 0.5
        #self.OffDuration_s = 0.5
        self.outputPin = getattr(pibrella.output, outputPin)

    # --------------------------------------------------------------------------
    def __enter__(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        logger.debug('Entering vibration motor %s', self.Name)
        return self

    # --------------------------------------------------------------------------
    def __exit__(self, type, value, traceback):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        logger.debug('Exiting vibration motor %s', self.Name)
        self.stop()

    # --------------------------------------------------------------------------
    def start(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        logger.debug('Started vibration motor \"%s\".', self.Name)
        self.outputPin.on()

    # --------------------------------------------------------------------------
    def stop(self):
        """TODO strictly one-line summary

        TODO Detailed multi-line description if
        necessary.

        Args:
            arg1 (type1): TODO describe arg, valid values, etc.
            arg2 (type2): TODO describe arg, valid values, etc.
            arg3 (type3): TODO describe arg, valid values, etc.
        Returns:
            TODO describe the return type and details
        Raises:
            TodoError1: if TODO.
            TodoError2: if TODO.

        """
        logger.debug('Stopped vibration motor \"%s\".', self.Name)
        self.outputPin.off()


# ------------------------------------------------------------------------------
# Module Initialization
# ------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # TODO - delete
handler = logging.handlers.SysLogHandler(address = '/dev/log')
logger.addHandler(handler)

