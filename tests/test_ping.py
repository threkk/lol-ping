# -*- coding: utf-8 -*-

""" Test suite for the function src.lol_ping.ping """
import unittest
from .context import ping


class PingTest(unittest.TestCase):
    """ Defines the tests of the suite. """

    def test_invalid_url(self):
        """ Tests if given an invalid string as url, it returns false. """
        output = ping('not a url')
        self.assertFalse(output)

    def test_timeout(self):
        """ Tests if in case of time out, it returns false. """
        output = ping('0.0.0.0')
        self.assertFalse(output)

    def test_valid_url(self):
        """
        Tests if in case the function is successful, it return an array
        with exactly 3 elements.
        """
        output = ping('8.8.8.8')
        self.assertTrue(output)
        self.assertTrue(len(output) == 3)

if __name__ == '__main__':
    unittest.main()
