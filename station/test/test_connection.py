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

from mock import MagicMock
from mock import Mock
from mock import patch
import sys
import unittest

sys.modules['flask'] = MagicMock()
from station.connection import ConnectionManager
from station.state import State

# ------------------------------------------------------------------------------
class ConnectionManagerTestCase(unittest.TestCase):
    """
    TODO class comment
    """

    # --------------------------------------------------------------------------
    def setUp(self):
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

        station = Mock()
        stationTypeId = 'hoiven-glaven'
        config = Mock()
        config.ResetUrlRule = '/path/to/reset/<int:pin>'
        config.StartChallengeUrlRule = '/path/to/sc'
        config.HandleSubmissionUrlRule = '/path/to/hs'
        config.ShutdownUrlRule = '/path/to/hd'

        self.Target = ConnectionManager(station, stationTypeId, config)


    # --------------------------------------------------------------------------
    def test_connected(self):
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

        # TODO
        #target = Led(name)
        #self.assertEqual(name, target.Name)


    # --------------------------------------------------------------------------
    def test_enter(self):
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

        # TODO
        #output = pibrella.output.e
        #self.assertEqual(0, output.read())
        #self.Target.turnOn()
        #self.assertEqual(1, output.read())


    # --------------------------------------------------------------------------
    def test_exit(self):
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

        # TODO
        #output = pibrella.output.f
        #self.assertEqual(0, output.read())
        #self.Target.turnOff()
        #self.assertEqual(1, output.read())


    # --------------------------------------------------------------------------
    def test_run(self):
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

        # TODO
        #self.Target.setFlashing()
        # TODO

    # --------------------------------------------------------------------------
    def test_startListening(self):
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

        # TODO
        #self.Target.setFlashing()
        # TODO

    # --------------------------------------------------------------------------
    def test_stopListening(self):
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

        # TODO
        #self.Target.setFlashing()
        # TODO

    # --------------------------------------------------------------------------
    def test_timestamp(self):
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

        # TODO
        #self.Target.setFlashing()
        # TODO

    # --------------------------------------------------------------------------
    def test_callService(self):
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

        # TODO
        #self.Target.setFlashing()
        # TODO

    # --------------------------------------------------------------------------
    def test_join(self):
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

        # TODO
        #self.Target.setFlashing()
        # TODO

    # --------------------------------------------------------------------------
    def test_leave(self):
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

        # TODO
        #self.Target.setFlashing()
        # TODO

    # --------------------------------------------------------------------------
    def test_timeExpired(self):
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

        # TODO
        #self.Target.setFlashing()
        # TODO

    # --------------------------------------------------------------------------
    def test_submitCtsComboToMS(self):
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

        # TODO
        #self.Target.setFlashing()
        # TODO

    # --------------------------------------------------------------------------
    def test_submitCpaDetectionToMS(self):
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

        # TODO
        #self.Target.setFlashing()
        # TODO

    # --------------------------------------------------------------------------
    @patch('station.connection.logger')
    def test_resetExpectedPin(self,
                              mock_logger):
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

        self._callback = Mock()
        self._callback.State = State.PROCESSING
        self.Target._resetPin = 'expectedPin'
        pin = self.Target._resetPin
        resp = self.Target.reset(pin)
        self.assertFalse(mock_logger.warning.called)
        self.assertEqual(State.READY, self.Target._callback.State, 'incorrect state: {}'.format(self._callback.State))
        self.assertEqual(200, resp.status_code)

    # --------------------------------------------------------------------------
    @patch('station.connection.logger')
    def test_resetUnexpectedPin(self,
                                mock_logger):
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

        self._callback = Mock()
        self._callback.State = State.PROCESSING
        self.Target._resetPin = 'expectedPin'
        pin = 'unexpectedPin'
        resp = self.Target.reset(pin)
        self.assertTrue(mock_logger.warning.called)
        self.assertEqual(State.PROCESSING, self._callback.State)
        self.assertEqual(400, resp.status_code)

    # --------------------------------------------------------------------------
    def test_startChallenge(self):
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

        # TODO
        #self.Target.setFlashing()
        # TODO

    # --------------------------------------------------------------------------
    def test_handleSubmission(self):
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

        # TODO
        #self.Target.setFlashing()
        # TODO

    # --------------------------------------------------------------------------
    def test_shutdown(self):
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

        # TODO
        #self.Target.setFlashing()
        # TODO


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
